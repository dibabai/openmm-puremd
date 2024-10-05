//
// Created by babaid on 05.10.24.
//

#include "openmm/ExternalPuremdForce.h"
#include "openmm/Force.h"
#include "openmm/OpenMMException.h"
#include "openmm/internal/AssertionUtilities.h"
#include "openmm/internal/ExternalPuremdForceImpl.h"

using namespace OpenMM;
using namespace std;

ExternalPuremdForce::ExternalPuremdForce(const std::string& ffield_file, const std::string& control_file) :usePeriodic(false), numContexts(0), ffield_file(ffield_file), control_file(control_file) {
}

int ExternalPuremdForce::addAtom(int particle, char symbol, bool isQM) {
    atoms.push_back(AtomInfo(particle, symbol, isQM));
    return atoms.size()-1;
}

void ExternalPuremdForce::getParticleParameters(int index, int &particle, char &symbol, int &isQM)  const {
    ASSERT_VALID_INDEX(index, atoms)
    particle = atoms[index].particle;
    symbol = atoms[index].symbol;
    isQM = static_cast<int>(atoms[index].isQM);
}

ForceImpl*ExternalPuremdForce::createImpl() const {
    if (numContexts == 0) {
        // Begin tracking changes to atoms.
        firstChangedBond = atoms.size();
        lastChangedBond = -1;
    }
    numContexts++;
    return new ExternalPuremdForceImpl(*this);
}

void ExternalPuremdForce::updateParametersInContext(Context& context) {
    dynamic_cast<ExternalPuremdForceImpl &>(getImplInContext(context)).updateParametersInContext(getContextImpl(context), firstChangedBond, lastChangedBond);
    if (numContexts == 1) {
        // We just updated the only existing context for this force, so we can reset
        // the tracking of changed atoms.
        firstChangedBond = atoms.size();
        lastChangedBond = -1;
    }
}

