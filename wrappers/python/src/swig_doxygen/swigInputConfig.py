# This file contains all API version specific info.  Should only need editing
# for major changes in the OpenMM API.

# Add base classes missing from the XML input file
MISSING_BASE_CLASSES = {'OpenMMException':'std::exception'}

# Doc strings to replace some fo the confusing ones generaged by swig
# Indexed by (className, methodName)
DOC_STRINGS = {("Context", "setPositions") :
                "setPositions(self, positions)",
               ("Context", "setVelocities") :
                "setVelocities(self, velocities)"}

# Do not generate wrappers for the following methods.
# Indexed by (className, [methodName [, numParams]])
SKIP_METHODS = [('State', 'getPositions'),
                ('State', 'getVelocities'),
                ('State', 'getForces'),
                ('StateBuilder',),
                ('Vec3',),
                ('OpenMMException',),
                ('AngleInfo',),
                ('ApplyAndersenThermostatKernel',),
                ('ApplyConstraintsKernel',),
                ('ApplyMonteCarloBarostatKernel',),
                ('BondInfo',),
                ('BondParameterInfo',),
                ('CalcAmoebaGeneralizedKirkwoodForceKernel',),
                ('CalcAmoebaMultipoleForceKernel',),
                ('CalcAmoebaTorsionTorsionForceKernel',),
                ('CalcAmoebaVdwForceKernel',),
                ('CalcAmoebaWcaDispersionForceKernel',),
                ('CalcCMAPTorsionForceKernel',),
                ('CalcCustomBondForceKernel',),
                ('CalcCustomCompoundBondForceKernel',),
                ('CalcCustomExternalForceKernel',),
                ('CalcCustomAngleForceKernel',),
                ('CalcCustomGBForceKernel',),
                ('CalcCustomHbondForceKernel',),
                ('CalcCustomNonbondedForceKernel',),
                ('CalcCustomTorsionForceKernel',),
                ('CalcForcesAndEnergyKernel',),
                ('CalcGBSAOBCForceKernel',),
                ('CalcHarmonicAngleForceKernel',),
                ('CalcHarmonicBondForceKernel',),
                ('CalcExternalPuremdForceKernel',),
                ('CalcNonbondedForceKernel',),
                ('CalcPeriodicTorsionForceKernel',),
                ('CalcRBTorsionForceKernel',),
                ('ComputationInfo',),
                ('ConstraintInfo',),
                ('CudaKernelFactory',),
                ('HipKernelFactory',),
                ('ExceptionInfo',),
                ('ExclusionInfo',),
                ('FunctionInfo',),
                ('GlobalParameterInfo',),
                ('IntegrateBrownianStepKernel',),
                ('IntegrateNoseHooverStepKernel',),
                ('IntegrateVariableLangevinStepKernel',),
                ('IntegrateVariableVerletStepKernel',),
                ('IntegrateVerletStepKernel',),
                ('IntegrateCustomStepKernel',),
                ('Kernel',),
                ('KernelFactory',),
                ('KernelImpl',),
                ('MultipoleInfo',),
                ('ParameterInfo',),
                ('ParticleInfo',),
                ('PeriodicTorsionInfo',),
                ('PerParticleParameterInfo',),
                ('PlatformData',),
                ('RBTorsionInfo',),
                ('RemoveCMMotionKernel',),
                ('SplineFitter',),
                ('TorsionInfo',),
                ('TorsionTorsionGridInfo',),
                ('TorsionTorsionInfo',),
                ('UpdateStateDataKernel',),
                ('VdwInfo',),
                ('WcaDispersionInfo',),
                ('Context',  'getIntegrator'),
                ('Context',  'createCheckpoint'),
                ('Context',  'loadCheckpoint'),
                ('CudaPlatform',),
                ('HipPlatform',),
                ('Force',    'Force'),
                ('ParticleParameterInfo',),
                ('Platform', 'contextCreated'),
                ('Platform', 'contextDestroyed'),
                ('Platform', 'createKernel'),
                ('Platform', 'registerKernelFactory'),
                ('IntegrateRPMDStepKernel',),
                ('CalcDrudeForceKernel',),
                ('IntegrateDrudeLangevinStepKernel',),
                ('IntegrateDrudeSCFStepKernel',),
                ('XmlSerializer',  'serialize'),
                ('XmlSerializer',  'deserialize'),
                ('LocalCoordinatesSite',  'getOriginWeights', 0),
                ('LocalCoordinatesSite',  'getXWeights', 0),
                ('LocalCoordinatesSite',  'getYWeights', 0),
                ("NoseHooverIntegrator", "getAllThermostatedIndividualParticles"),
                ("NoseHooverIntegrator", "getAllThermostatedPairs"),
]




# The build script assumes method args that are non-const references are
# used to output values. This list gives exceptions to this rule.
NO_OUTPUT_ARGS = [('LocalEnergyMinimizer', 'minimize', 'context'),
                  ('Platform', 'setPropertyValue', 'context'),
                  ('AmoebaTorsionTorsionForce', 'setTorsionTorsionGrid', 'grid'),
                  ('AmoebaVdwForce', 'setParticleExclusions', 'exclusions'),
                  ('AmoebaMultipoleForce', 'addParticle', 'molecularDipole'),
                  ('AmoebaMultipoleForce', 'addParticle', 'molecularQuadrupole'),
                  ('AmoebaMultipoleForce', 'setCovalentMap', 'covalentAtoms'),
                  ('AmoebaMultipoleForce', 'getElectrostaticPotential', 'context'),
                  ('AmoebaMultipoleForce', 'getInducedDipoles', 'context'),
                  ('AmoebaMultipoleForce', 'getLabFramePermanentDipoles', 'context'),
                  ('AmoebaMultipoleForce', 'getTotalDipoles', 'context'),
                  ('HippoNonbondedForce', 'addParticle', 'dipole'),
                  ('HippoNonbondedForce', 'addParticle', 'quadrupole'),
                  ('HippoNonbondedForce', 'getInducedDipoles', 'context'),
                  ('HippoNonbondedForce', 'getLabFramePermanentDipoles', 'context'),
]

# SWIG assumes the target language shadow class owns the C++ class
# so by default, when the  shadow class is deleted, the C++ class is also.
# However, if a class is passed to another class, it may be appropriate to
# change this.  The following dict lists the (Class,Methods) for which the
# shadow class should *lose* ownership of the C++ class.
# The list is the argument position(s).
STEAL_OWNERSHIP = {("Platform", "registerPlatform") : [0],
                   ("System", "addForce") : [0],
                   ("System", "setVirtualSite") : [1],
                   ("ATMForce", "addForce") : [0],
                   ("CustomNonbondedForce", "addTabulatedFunction") : [1],
                   ("CustomGBForce", "addTabulatedFunction") : [1],
                   ("CustomHbondForce", "addTabulatedFunction") : [1],
                   ("CustomCentroidBondForce", "addTabulatedFunction") : [1],
                   ("CustomCompoundBondForce", "addTabulatedFunction") : [1],
                   ("CustomManyParticleForce", "addTabulatedFunction") : [1],
                   ("CustomCVForce", "addTabulatedFunction") : [1],
                   ("CustomCVForce", "addCollectiveVariable") : [1],
                   ("CustomIntegrator", "addTabulatedFunction") : [1],
                   ("CompoundIntegrator", "addIntegrator") : [0],
}


REQUIRE_ORDERED_SET = {("CustomNonbondedForce", "addInteractionGroup") : [0, 1],
                       ("CustomNonbondedForce", "setInteractionGroupParameters") : [1, 2],
}


# This is a list of units to attach to return values and method args.
# Indexed by (ClassName, MethodsName)
UNITS = {
("*", "getConstraintTolerance") : (None, ()),
("*", "getCutoffDistance") : ("unit.nanometers", ()),
("*", "setCutoffDistance") : (None, ("unit.nanometers",)),
("*", "getSwitchingDistance") : ("unit.nanometers", ()),
("*", "setSwitchingDistance") : (None, ("unit.nanometers",)),
("*", "getDefaultCollisionFrequency") : ("unit.picosecond**-1", ()),
("*", "setDefaultCollisionFrequency") : (None, ("unit.picosecond**-1",)),
("*", "getDefaultPeriodicBoxVectors") : (None, ("unit.nanometer", "unit.nanometer", "unit.nanometer")),
("*", "setDefaultPeriodicBoxVectors") : (None, ("unit.nanometer", "unit.nanometer", "unit.nanometer")),
("*", "getDefaultPressure") : ("unit.bar", ()),
("*", "getDefaultPressureX") : ("unit.bar", ()),
("*", "getDefaultPressureY") : ("unit.bar", ()),
("*", "getDefaultPressureZ") : ("unit.bar", ()),
("*", "setDefaultPressure") : (None, ("unit.bar",)),
("*", "setDefaultPressureX") : (None, ("unit.bar",)),
("*", "setDefaultPressureY") : (None, ("unit.bar",)),
("*", "setDefaultPressureZ") : (None, ("unit.bar",)),
("*", "getDefaultSurfaceTension") : ("unit.bar*unit.nanometer", ()),
("*", "setDefaultSurfaceTension") : (None, ("unit.bar*unit.nanometer",)),
("*", "getDefaultTemperature") : ("unit.kelvin", ()),
("*", "setDefaultTemperature") : (None, ("unit.kelvin",)),
("*", "getRelativeTemperature") : ("unit.kelvin", ()),
("*", "getErrorTolerance") : (None, ()),
("*", "getEwaldErrorTolerance") : (None, ()),
("*", "getFriction") : ("unit.picosecond**-1", ()),
("*", "setFriction") : (None, ("unit.picosecond**-1",)),
("*", "getGlobalVariable") : (None, ()),
("*", "getGlobalVariableByName") : (None, ()),
("*", "getIntegrator") : (None, ()),
("*", "getMapParameters") : (None, ()),
("*", "getName") : (None, ()),
("*", "getNumAngles") : (None, ()),
("*", "getNumBonds") : (None, ()),
("*", "getNumConstraints") : (None, ()),
("*", "getNumExceptions") : (None, ()),
("*", "getNumForces") : (None, ()),
("*", "getNumMaps") : (None, ()),
("*", "getNumParticles") : (None, ()),
("*", "getNumPlatforms") : (None, ()),
("*", "getNumTorsions") : (None, ()),
("*", "getOpenMMVersion") : (None, ()),
("*", "getParticleMass") : ("unit.amu", ()),
("*", "setParticleMass") : (None, (None, "unit.amu")),
("*", "getPlatform") : (None, ()),
("*", "getPlatformByName") : (None, ()),
("*", "getPluginLoadFailures"): (None, ()),
("*", "getRandomNumberSeed") : (None, ()),
("*", "getReactionFieldDielectric") : (None, ()),
("*", "getSoluteDielectric") : (None, ()),
("*", "getSolventDielectric") : (None, ()),
("*", "getStepSize") : ("unit.picosecond", ()),
("*", "setStepSize") : (None, ("unit.picosecond",)),
("*", "getMaximumStepSize") : ("unit.picosecond", ()),
("*", "setMaximumStepSize") : (None, ("unit.picosecond",)),
("*", "getSystem") : (None, ()),
("*", "getTabulatedFunction") : (None, ()),
("*", "getUseDispersionCorrection") : (None, ()),
("*", "getTemperature") : ("unit.kelvin", ()),
("*", "getCollisionFrequency") : ( "unit.picosecond**-1", ()),
("*", "getRelativeCollisionFrequency") : ( "unit.picosecond**-1", ()),
("*", "getUseDispersionCorrection") : (None, ()),
("*", "getWeight") : (None, ()),
("*", "getWeight12") : (None, ()),
("*", "getWeight13") : (None, ()),
("*", "getWeightCross") : (None, ()),
("*", "getNonbondedMethod") : (None, ()),
("*", "getGlobalParameterDefaultValue") : (None, ()),
("*", "getPermutationMode") : (None, ()),
("*", "computeSystemTemperature") : ("unit.kelvin", ()),
("*", "computeDrudeTemperature") : ("unit.kelvin", ()),
("LocalCoordinatesSite", "getOriginWeights") : (None, ()),
("LocalCoordinatesSite", "getXWeights") : (None, ()),
("LocalCoordinatesSite", "getYWeights") : (None, ()),
("LocalCoordinatesSite", "getLocalPosition") : ("unit.nanometer", ()),
("SerializationNode", "getChildren") : (None, ()),
("SerializationNode", "getChildNode") : (None, ()),
("SerializationNode", "getProperties") : (None, ()),
("SerializationNode", "getStringProperty") : (None, ()),
("SerializationNode", "getIntProperty") : (None, ()),
("SerializationNode", "getLongProperty") : (None, ()),
("SerializationNode", "getDoubleProperty") : (None, ()),
("SerializationProxy", "getProxy") : (None, ()),
("SerializationProxy", "getTypeName") : (None, ()),

# check getSurfaceAreaFactor
("AmoebaGeneralizedKirkwoodForce",       "getParticleParameters")                         :  (None, ('unit.elementary_charge', 'unit.nanometer', None)),
("AmoebaGeneralizedKirkwoodForce",       "getDielectricOffset")                           :  ( 'unit.nanometer', ()),
("AmoebaGeneralizedKirkwoodForce",       "getIncludeCavityTerm")                          :  ( None,()),
("AmoebaGeneralizedKirkwoodForce",       "getProbeRadius")                                :  ( 'unit.nanometer', ()),
("AmoebaGeneralizedKirkwoodForce",       "getSurfaceAreaFactor")                          :  ( 'unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)',()),

("AmoebaMultipoleForce",                 "getNumMultipoles")                              :  ( None,()),
("AmoebaMultipoleForce",                 "getPolarizationType")                           :  ( None,()),
("AmoebaMultipoleForce",                 "getCutoffDistance")                             :  (  'unit.nanometer',()),
("AmoebaMultipoleForce",                 "getAEwald")                                     :  (  '1/unit.nanometer',()),
("AmoebaMultipoleForce",                 "getPmeBSplineOrder")                            :  ( None,()),
("AmoebaMultipoleForce",                 "getMutualInducedMaxIterations")                 :  ( None, ()),
("AmoebaMultipoleForce",                 "getMutualInducedTargetEpsilon")                 :  ( None, ()),
("AmoebaMultipoleForce",                 "getExtrapolationCoefficients")                            :  ( None, ()),
("AmoebaMultipoleForce",                 "getEwaldErrorTolerance")                        :  ( None, ()),
("AmoebaMultipoleForce",                 "getPmeGridDimensions")                          :  ( None,()),

# AmoebaMultipoleForce methods starting w/ getMultipoleParameters need work

# dipoleConversion        = AngstromToNm;
# quadrupoleConversion    = AngstromToNm*AngstromToNm;
# polarityConversion      = AngstromToNm*AngstromToNm*AngstromToNm;
# dampingFactorConversion = sqrt( AngstromToNm );

#    void getMultipoleParameters(int index, double& charge, std::vector<double>& molecularDipole, std::vector<double>& molecularQuadrupole,
#                                int& axisType, int& multipoleAtomZ, int& multipoleAtomX, int& multipoleAtomY, double& thole, double& dampingFactor, double& polarity ) const;
#    void getCovalentMap(int index, CovalentType typeId, std::vector<int>& covalentAtoms )
#    void getCovalentMaps(int index, std::vector < std::vector<int> >& covalentLists )

("AmoebaMultipoleForce",                 "getMultipoleParameters")                        :  ( None, ('unit.elementary_charge', 'unit.elementary_charge*unit.nanometer',
                                                                                                      'unit.elementary_charge*unit.nanometer**2', None, None, None, None, None, None,
                                                                                                      'unit.nanometer**3')),
("AmoebaMultipoleForce",                 "getCovalentMap")                                :  ( None, ()),
("AmoebaMultipoleForce",                 "getCovalentMaps")                               :  ( None, ()),
("AmoebaMultipoleForce",                 "getScalingDistanceCutoff")                      :  ( 'unit.nanometer', ()),
("AmoebaMultipoleForce",                 "getElectricConstant")                           :  ( None, ()),
#("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( None, ('unit.kilojoule_per_mole')),
#("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( ('unit.kilojoule_per_mole'), ()),
("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( None, ()),
("AmoebaMultipoleForce",                 "getInducedDipoles")                             :  ( None, ()),
("AmoebaMultipoleForce",                 "getLabFramePermanentDipoles")                   :  ( None, ()),
("AmoebaMultipoleForce",                 "getTotalDipoles")                               :  ( None, ()),
("AmoebaMultipoleForce",                 "getSystemMultipoleMoments")                     :  ( None, ()),

("AmoebaTorsionTorsionForce",             "getNumTorsionTorsions")                         :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getNumTorsionTorsionGrids")                     :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getTorsionTorsionParameters")                   :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getTorsionTorsionGrid")                         :  ( None, ()),

("AmoebaVdwForce",                        "getSigmaCombiningRule")                         :  ( None, ()),
("AmoebaVdwForce",                        "getEpsilonCombiningRule")                       :  ( None, ()),
("AmoebaVdwForce",                        "getParticleExclusions")                         :  ( None, ()),
("AmoebaVdwForce",                        "getAlchemicalMethod")                           :  ( None, ()),
("AmoebaVdwForce",                        "getPotentialFunction")                          :  ( None, ()),
("AmoebaVdwForce",                        "getSoftcorePower")                              :  ( None, ()),
("AmoebaVdwForce",                        "getSoftcoreAlpha")                              :  ( None, ()),
("AmoebaVdwForce",                        "getCutoff")                                     :  ( 'unit.nanometer', ()),
("AmoebaVdwForce",                        "getParticleParameters")                         :  ( None, (None, 'unit.nanometer', 'unit.kilojoule_per_mole', None, None, None)),
("AmoebaVdwForce",                        "getParticleTypeParameters")                     :  ( None, ('unit.nanometer', 'unit.kilojoule_per_mole')),
("AmoebaVdwForce",                        "getTypePairParameters")                         :  ( None, (None, None, 'unit.nanometer', 'unit.kilojoule_per_mole')),

("AmoebaWcaDispersionForce",              "getParticleParameters")                         :  ( None, ('unit.nanometer', 'unit.kilojoule_per_mole')),
("AmoebaWcaDispersionForce",              "getAwater")                                     :  ( '1/(unit.nanometer*unit.nanometer*unit.nanometer)',()),
("AmoebaWcaDispersionForce",              "getDispoff")                                    :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getRmino")                                      :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getRminh")                                      :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getEpso")                                       :  ( 'unit.kilojoule_per_mole',()),
("AmoebaWcaDispersionForce",              "getEpsh")                                       :  ( 'unit.kilojoule_per_mole',()),
("AmoebaWcaDispersionForce",              "getSlevy")                                      :  ( None, ()),
("AmoebaWcaDispersionForce",              "getShctd")                                      :  ( None, ()),

("HippoNonbondedForce",                 "getExtrapolationCoefficients")                  :  ( None, ()),
("HippoNonbondedForce",                 "getParticleParameters")                         :  ( None, ('unit.elementary_charge', 'unit.elementary_charge*unit.nanometer',
                                                                                                      'unit.elementary_charge*unit.nanometer**2', 'unit.elementary_charge',
                                                                                                       None, None, None, None, None, None, None, None, None, None, None, None)),
("HippoNonbondedForce",                 "getInducedDipoles")                             :  ( None, ()),
("HippoNonbondedForce",                 "getLabFramePermanentDipoles")                   :  ( None, ()),
    
("Context", "getParameter") : (None, ()),
("Context", "getParameters") : (None, ()),
("Context", "getMolecules") : (None, ()),
("Context", "getState") : (None, (None, None, None)),
("Context", "setPeriodicBoxVectors") : (None, ("unit.nanometer", "unit.nanometer", "unit.nanometer")),
("Context", "setPositions") : (None, ("unit.nanometer",)),
("Context", "getTime") : ("unit.picosecond", ()),
("Context", "setTime") : (None, ("unit.picosecond",)),
("Context", "getStepCount") : (None, ()),
("Context", "setStepCount") : (None, (None,)),
("Context", "setVelocities") : (None, ("unit.nanometer/unit.picosecond",)),
("CMAPTorsionForce", "getMapParameters") : (None, (None, "unit.kilojoule_per_mole")),
("CMAPTorsionForce", "setMapParameters") : (None, (None, None, "unit.kilojoule_per_mole")),
("CMAPTorsionForce", "getTorsionParameters") : (None, ()),
("CMMotionRemover", "getFrequency") : (None, ()),
("CustomAngleForce", "getNumPerAngleParameters") : (None, ()),
("CustomAngleForce", "getNumGlobalParameters") : (None, ()),
("CustomAngleForce", "getEnergyFunction") : (None, ()),
("CustomAngleForce", "getPerAngleParameterName") : (None, ()),
("CustomAngleForce", "getGlobalParameterName") : (None, ()),
("CustomAngleForce", "getAngleParameters") : (None, ()),
("CustomBondForce", "getNumPerBondParameters") : (None, ()),
("CustomBondForce", "getNumGlobalParameters") : (None, ()),
("CustomBondForce", "getEnergyFunction") : (None, ()),
("CustomBondForce", "getPerBondParameterName") : (None, ()),
("CustomBondForce", "getGlobalParameterName") : (None, ()),
("CustomBondForce", "getBondParameters") : (None, ()),
("CustomExternalForce", "getNumPerParticleParameters") : (None, ()),
("CustomExternalForce", "getNumGlobalParameters") : (None, ()),
("CustomExternalForce", "getEnergyFunction") : (None, ()),
("CustomExternalForce", "getPerParticleParameterName") : (None, ()),
("CustomExternalForce", "getGlobalParameterName") : (None, ()),
("CustomExternalForce", "getParticleParameters") : (None, ()),
("CustomGBForce", "getNumExclusions") : (None, ()),
("CustomGBForce", "getNumPerParticleParameters") : (None, ()),
("CustomGBForce", "getNumGlobalParameters") : (None, ()),
("CustomGBForce", "getNumFunctions") : (None, ()),
("CustomGBForce", "getNumComputedValues") : (None, ()),
("CustomGBForce", "getNumEnergyTerms") : (None, ()),
("CustomGBForce", "getPerParticleParameterName") : (None, ()),
("CustomGBForce", "getGlobalParameterName") : (None, ()),
("CustomGBForce", "getParticleParameters") : (None, ()),
("CustomGBForce", "getComputedValueParameters") : (None, ()),
("CustomGBForce", "getEnergyTermParameters") : (None, ()),
("CustomGBForce", "getExclusionParticles") : (None, ()),
("CustomGBForce", "getFunctionParameters") : (None, ()),
("CustomHbondForce", "getAcceptorParameters") : (None, ()),
("CustomHbondForce", "getDonorParameters") : (None, ()),
("CustomHbondForce", "getEnergyFunction") : (None, ()),
("CustomHbondForce", "getExclusionParticles") : (None, ()),
("CustomHbondForce", "getFunctionParameters") : (None, ()),
("CustomHbondForce", "getNumAcceptors") : (None, ()),
("CustomHbondForce", "getNumDonors") : (None, ()),
("CustomHbondForce", "getNumExclusions") : (None, ()),
("CustomHbondForce", "getNumFunctions") : (None, ()),
("CustomHbondForce", "getNumGlobalParameters") : (None, ()),
("CustomHbondForce", "getNumPerAcceptorParameters") : (None, ()),
("CustomHbondForce", "getNumPerDonorParameters") : (None, ()),
("CustomHbondForce", "getGlobalParameterName") : (None, ()),
("CustomHbondForce", "getPerAcceptorParameterName") : (None, ()),
("CustomHbondForce", "getPerDonorParameterName") : (None, ()),
("CustomNonbondedForce", "getEnergyFunction") : (None, ()),
("CustomNonbondedForce", "getExceptionParameters") : (None, ()),
("CustomNonbondedForce", "getExclusionParticles") : (None, ()),
("CustomNonbondedForce", "getFunctionParameters") : (None, ()),
("CustomNonbondedForce", "getGlobalParameterName") : (None, ()),
("CustomNonbondedForce", "getNumExclusions") : (None, ()),
("CustomNonbondedForce", "getNumFunctions") : (None, ()),
("CustomNonbondedForce", "getNumPerParticleParameters") : (None, ()),
("CustomNonbondedForce", "getNumParameters") : (None, ()),
("CustomNonbondedForce", "getNumGlobalParameters") : (None, ()),
("CustomNonbondedForce", "getParameterCombiningRule") : (None, ()),
("CustomNonbondedForce", "getParameterName") : (None, ()),
("CustomNonbondedForce", "getParticleParameters") : (None, ()),
("CustomNonbondedForce", "getPerParticleParameterName") : (None, ()),
("CustomTorsionForce", "getNumPerTorsionParameters") : (None, ()),
("CustomTorsionForce", "getNumGlobalParameters") : (None, ()),
("CustomTorsionForce", "getEnergyFunction") : (None, ()),
("CustomTorsionForce", "getPerTorsionParameterName") : (None, ()),
("CustomTorsionForce", "getGlobalParameterName") : (None, ()),
("CustomTorsionForce", "getTorsionParameters") : (None, ()),
("CustomCVForce", "getCollectiveVariable") : (None, ()),
("CustomCVForce", "getInnerContext") : (None, ()),
("DrudeForce", "addParticle") : (None, (None, None, None, None, None, "unit.elementary_charge", "unit.nanometer**3", None, None)),
("DrudeForce", "getParticleParameters") : (None, (None, None, None, None, None, "unit.elementary_charge", "unit.nanometer**3", None, None)),
("DrudeForce", "setParticleParameters") : (None, (None, None, None, None, None, None, "unit.elementary_charge", "unit.nanometer**3", None, None)),
("DrudeForce", "getNumScreenedPairs") : (None, ()),
("DrudeForce", "getScreenedPairParameters") : (None, ()),
("GBSAOBCForce", "addParticle") : (None, ("unit.elementary_charge", "unit.nanometer", None)),
("GBSAOBCForce", "getParticleParameters") : (None, ("unit.elementary_charge", "unit.nanometer", None)),
("GBSAOBCForce", "setParticleParameters") : (None, (None, "unit.elementary_charge", "unit.nanometer", None)),
("GBSAOBCForce", "getSurfaceAreaEnergy") : ("unit.kilojoule_per_mole/unit.nanometer/unit.nanometer", ()),
("GBSAOBCForce", "setSurfaceAreaEnergy") : (None, ("unit.kilojoule_per_mole/unit.nanometer/unit.nanometer",)),
("HarmonicAngleForce", "addAngle") : (None, (None, None, None, "unit.radian", "unit.kilojoule_per_mole/(unit.radian*unit.radian)")),
("HarmonicAngleForce", "getAngleParameters") : (None, (None, None, None, "unit.radian", "unit.kilojoule_per_mole/(unit.radian*unit.radian)")),
("HarmonicAngleForce", "setAngleParameters") : (None, (None, None, None, None, "unit.radian", "unit.kilojoule_per_mole/(unit.radian*unit.radian)")),
("HarmonicBondForce", "addBond") : (None, (None, None, "unit.nanometer", "unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)")),
("HarmonicBondForce", "getBondParameters") : (None, (None, None, "unit.nanometer", "unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)")),
("HarmonicBondForce", "setBondParameters") : (None, (None, None, None, "unit.nanometer", "unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)")),
("MonteCarloBarostat", "getFrequency") : (None, ()),
("MonteCarloAnisotropicBarostat", "getFrequency") : (None, ()),
("NonbondedForce", "getPMEParameters") : (None, ("unit.nanometer**-1", None, None, None)),
("NonbondedForce", "setPMEParameters") : (None, ("unit.nanometer**-1", None, None, None)),
("NonbondedForce", "addException") : (None, (None, None, "unit.elementary_charge*unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("NonbondedForce", "getExceptionParameters") : (None, (None, None, "unit.elementary_charge*unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("NonbondedForce", "setExceptionParameters") : (None, (None, None, None, "unit.elementary_charge*unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("NonbondedForce", "addParticle") : (None, ("unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("NonbondedForce", "getParticleParameters") : (None, ("unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("NonbondedForce", "setParticleParameters") : (None, (None, "unit.elementary_charge", "unit.nanometer", "unit.kilojoule_per_mole")),
("PeriodicTorsionForce", "addTorsion") : (None, (None, None, None, None, None, "unit.radian", "unit.kilojoule_per_mole")),
("PeriodicTorsionForce", "getTorsionParameters") : (None, (None, None, None, None, None, "unit.radian", "unit.kilojoule_per_mole")),
("PeriodicTorsionForce", "setTorsionParameters") : (None, (None, None, None, None, None, None, "unit.radian", "unit.kilojoule_per_mole")),
("GayBerneForce", "addParticle") : (None, ("unit.nanometer", "unit.kilojoule_per_mole", None, None, "unit.nanometer", "unit.nanometer", "unit.nanometer", None, None, None)),
("GayBerneForce", "getParticleParameters") : (None, ("unit.nanometer", "unit.kilojoule_per_mole", None, None, "unit.nanometer", "unit.nanometer", "unit.nanometer", None, None, None)),
("GayBerneForce", "setParticleParameters") : (None, (None, "unit.nanometer", "unit.kilojoule_per_mole", None, None, "unit.nanometer", "unit.nanometer", "unit.nanometer", None, None, None)),
("Platform", "getDefaultPluginsDirectory") : (None, ()),
("Platform", "getPropertyDefaultValue") : (None, ()),
("Platform", "getPropertyNames") : (None, ()),
("Platform", "getPropertyValue") : (None, ()),
("Platform", "getSpeed") : (None, ()),
("RBTorsionForce", "addTorsion") : (None, (None, None, None, None, "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole")),
("RBTorsionForce", "getTorsionParameters") : (None, (None, None, None, None, "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole")),
("RBTorsionForce", "setTorsionParameters") : (None, (None, None, None, None, None, "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole", "unit.kilojoules_per_mole")),
("State", "getTime") : ("unit.picosecond", ()),
("State", "getStepCount") : (None, ()),
("State", "getKineticEnergy") : ("unit.kilojoules_per_mole", ()),
("State", "getPotentialEnergy") : ("unit.kilojoules_per_mole", ()),
("State", "getPeriodicBoxVolume") : ("unit.nanometers**3", ()),
("State", "getPeriodicBoxVectors") : ("unit.nanometers", ()),
("State", "getParameters") : (None, ()),
("State", "getEnergyParameterDerivatives") : (None, ()),
("System", "addParticle") : (None, ("unit.amu",)),
("System", "addConstraint") : (None, (None, None, "unit.nanometer")),
("System", "getConstraintParameters") : (None, (None, None, "unit.nanometer")),
("System", "setConstraintParameters") : (None, (None, None, None, "unit.nanometer")),
("System", "getForce") : (None, ()),
("System", "getVirtualSite") : (None, ()),
("AndersenThemostat", "AndersenThemostat") : (None, ("unit.kelvin", "unit.picosecond**-1")),
("MonteCarloAnisotropicBarostat", "MonteCarloAnisotropicBarostat") : (None, ("unit.bar", "unit.kelvin", None, None, None, None)),
("MonteCarloBarostat", "MonteCarloBarostat") : (None, ("unit.bar", "unit.kelvin", None)),
("MonteCarloMembraneBarostat", "MonteCarloMembraneBarostat") : (None, ("unit.bar", "unit.bar*unit.nanometer", "unit.kelvin", None, None, None)),
("MonteCarloMembraneBarostat", "getXYMode") : (None, ()),
("MonteCarloMembraneBarostat", "getZMode") : (None, ()),
("CustomIntegrator", "CustomIntegrator") : (None, ("unit.picosecond",)),
("BrownianIntegrator", "BrownianIntegrator") : (None, ("unit.kelvin", "unit.picosecond**-1", "unit.picosecond")),
("LangevinIntegrator", "LangevinIntegrator") : (None, ("unit.kelvin", "unit.picosecond**-1", "unit.picosecond")),
("LangevinMiddleIntegrator", "LangevinMiddleIntegrator") : (None, ("unit.kelvin", "unit.picosecond**-1", "unit.picosecond")),
("VariableLangevinIntegrator", "VariableLangevinIntegrator") : (None, ("unit.kelvin", "unit.picosecond**-1", None)),
("VerletIntegrator", "VerletIntegrator") : (None, ("unit.picosecond",)),
("DrudeIntegrator", "getDrudeTemperature") : ("unit.kelvin", ()),
("DrudeIntegrator", "setDrudeTemperature") : (None, ("unit.kelvin",)),
("DrudeIntegrator", "getMaxDrudeDistance") : ("unit.nanometer", ()),
("DrudeIntegrator", "setMaxDrudeDistance") : (None, ("unit.nanometer",)),
("DrudeLangevinIntegrator", "getDrudeTemperature") : ("unit.kelvin", ()),
("DrudeLangevinIntegrator", "setDrudeTemperature") : (None, ("unit.kelvin",)),
("DrudeLangevinIntegrator", "getMaxDrudeDistance") : ("unit.nanometer", ()),
("DrudeLangevinIntegrator", "setMaxDrudeDistance") : (None, ("unit.nanometer",)),
("DrudeNoseHooverIntegrator", "getVelocitiesForTemperature") : ("unit.nanometers / unit.picosecond", (None, "unit.kelvin", None)),
("DrudeLangevinIntegrator", "getDrudeFriction") : ("unit.picosecond**-1", ()),
("DrudeLangevinIntegrator", "setDrudeFriction") : (None, ("unit.picosecond**-1",)),
("DrudeSCFIntegrator", "getMinimizationErrorTolerance") : ("unit.kilojoules_per_mole/unit.nanometer", ()),
("DrudeSCFIntegrator", "setMinimizationErrorTolerance") : (None, ("unit.kilojoules_per_mole/unit.nanometer",)),
("RPMDIntegrator", "getContractions") : (None, ()),
("RPMDIntegrator", "getTotalEnergy") : ("unit.kilojoules_per_mole", ()),
("RPMDIntegrator", "getState"): (None,(None, None, None, None)),
("RMSDForce", "getReferencePositions") : ("unit.nanometer", ()),
("RMSDForce", "setReferencePositions") : (None, ("unit.nanometer",)),
("RMSDForce", "getParticles") : (None, ()),
("NoseHooverChain", "NoseHooverChain") : (None, ("unit.kelvin", "unit.kelvin", "unit.picosecond**-1", "unit.picosecond**-1", None, None, None, None, None, None, None)),
("NoseHooverChain", "getThermostatedPairs") : (None, ()),
("NoseHooverChain", "getThermostatedAtoms") : (None, ()),
("NoseHooverChain", "getYoshidaSuzukiWeights") : (None, ()),
("NoseHooverIntegrator", "setTemperature") : (None, ("unit.kelvin", None)),
("NoseHooverIntegrator", "setRelativeTemperature") : (None, ("unit.kelvin", None) ),
("NoseHooverIntegrator", "setCollisionFrequency") : (None, ("unit.picosecond**-1", None)),
("NoseHooverIntegrator", "setRelativeCollisionFrequency") : (None, ("unit.picosecond**-1", None)),
("NoseHooverIntegrator", "computeHeatBathEnergy") : ( "unit.kilojoules_per_mole", ()),
("NoseHooverIntegrator", "addThermostat"): (None, ("unit.kelvin", "unit.picosecond**-1", None, None, None)),
("NoseHooverIntegrator", "addSubsystemThermostat"): (None, (None, None, "unit.kelvin", "unit.picosecond**-1", "unit.kelvin", "unit.picosecond**-1", None, None, None)),
("NoseHooverIntegrator", "getNumThermostats") : (None, ()),
("NoseHooverIntegrator", "getThermostat") : (None, ()),
("NoseHooverIntegrator", "getMaximumPairDistance") : ("unit.nanometer", ()),
("NoseHooverIntegrator", "setMaximumPairDistance") : (None, ("unit.nanometer",)),
("DrudeNoseHooverIntegrator", "getMaxDrudeDistance") : ("unit.nanometer", ()),
("DrudeNoseHooverIntegrator", "setMaxDrudeDistance") : (None, ("unit.nanometer",)),
("LocalEnergyMinimizer", "minimize") : (None, (None, "unit.kilojoules_per_mole/unit.nanometer", None)),
("ATMForce", "getForce") : (None, ()),
("ATMForce", "getPerturbationEnergy") :  ('unit.kilojoule_per_mole', ()),
("ATMForce", "getDefaultLambda1") :  (None, ()),
("ATMForce", "getDefaultLambda2") :  (None, ()),
("ATMForce", "getDefaultAlpha") :  ('unit.kilojoule_per_mole**-1', ()),
("ATMForce", "getDefaultU0") :  ('unit.kilojoule_per_mole', ()),
("ATMForce", "getDefaultW0") :  ('unit.kilojoule_per_mole', ()),
("ATMForce", "getDefaultDirection") :  (None, ()),
("ATMForce", "getDefaultUmax") :  ('unit.kilojoule_per_mole', ()),
("ATMForce", "getDefaultUbcore") :  ('unit.kilojoule_per_mole', ()),
("ATMForce", "getDefaultAcore") :  (None, ()),
("ATMForce", "getParticleParameters") : (None, ("unit.nanometer", "unit.nanometer")),
}
