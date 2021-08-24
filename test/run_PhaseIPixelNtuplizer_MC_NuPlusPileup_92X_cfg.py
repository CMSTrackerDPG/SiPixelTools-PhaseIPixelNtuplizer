# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: -s GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO --evt_type SingleNuE10_cfi --process PrivateMC --conditions auto:phase1_2017_realistic --era Run2_2017 --geometry DB:Extended --datatier GEN-SIM-RECO --eventcontent RECOSIM --pileup Flat_0_50_25ns --pileup_input dbs:/RelValMinBias_13/CMSSW_9_2_0-91X_upgrade2017_realistic_v5-v1/GEN-SIM --fileout file:PhaseI_GenNu_13TeV_FlatPileup0to50_RECO.root --python_filename PhaseI_GenNuPlusPileup_92X_cfg.py --runUnscheduled -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PrivateMC',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_Flat_0_50_25ns_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleNuE10_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:PhaseI_GenNu_13TeV_FlatPileup0to50_RECO.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/00521C9A-FF3B-E711-95CE-0025905B85BC.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/46B7E6CE-FF3B-E711-9842-0CC47A4D7644.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/782C6833-FF3B-E711-AE98-0025905B85B8.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/7C59CF8C-FE3B-E711-BFF4-0025905B8598.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/9EB191A8-003C-E711-ACA2-0025905A609E.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/BC49886A-003C-E711-BD6A-0025905A6090.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/C0555BA5-003C-E711-9503-0025905B8606.root', '/store/relval/CMSSW_9_2_0/RelValMinBias_13/GEN-SIM/91X_upgrade2017_realistic_v5-v1/10000/C252F75C-FE3B-E711-B39C-0025905B85B8.root'])
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxE = cms.double(10.01),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinE = cms.double(9.99),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        PartID = cms.vint32(12)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single Nu E 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 














# begin inserting configs
#------------------------------------------
#  Options - can be given from command line
#------------------------------------------
import FWCore.ParameterSet.VarParsing as opts

opt = opts.VarParsing ('analysis')

opt.register('globalTag',          '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Global Tag, Default="" which uses auto:phase1_2017_realistic')

opt.register('useTemplates',       True,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Only for On-track clusters! True: use Template reco, False: use Generic reco')

opt.register('saveRECO',           False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Option to keep GEN-SIM-RECO')

opt.register('useRECO',            False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Option to use GEN-SIM-RECO')

opt.register('RECOFileName',  '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Name of the histograms file')

opt.register('noMagField',         False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (SIM) conditions locally (prep/prod database or sqlite file')

opt.register('outputFileName',      '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Name of the histograms file')

opt.register('useLocalLASim',      False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (SIM) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalQuality',    False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Quality conditions locally (prep/prod database or sqlite file')

opt.register('useLocalLA',         False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (RECO) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGain',       False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Gain conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGenErr',     False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test GenError conditions locally (prep/prod database or sqlite file')

opt.register('useLocalTemplates',  False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Template conditions locally (prep/prod database or sqlite file')

opt.register('useLocalDynIneff',   False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Dynamic Inefficiency conditions locally (prep/prod database or sqlite file')

### Events to process: 'maxEvents' is already registered by the framework
opt.setDefault('maxEvents', 100)

# Proceed with settings from command line
opt.parseArguments()

process.maxEvents.input = opt.maxEvents
process.MessageLogger.cerr.FwkReport.reportEvery = 10

# Input GEN-SIM files
from SiPixelTools.PhaseIPixelNtuplizer.PoolSource_13TeV_92X_upgrade2017_realistic_v2_GS import *
process.mix.input.fileNames = pileupFileNames

# Add Input file in case using it
if opt.useRECO:
	process.setName_("TEST")
	process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
		# This is the file you create with saveRECO, by default
		opt.RECOFileName # Use previously saved RECO as input
		))

# Switch off magnetic field
if opt.noMagField:
	process.load('Configuration.StandardSequences.MagneticField_0T_cff')
	process.g4SimHits.UseMagneticField = cms.bool(False)


# Set some default options based on others
if opt.useTemplates:
	if opt.RECOFileName == '': opt.RECOFileName = 'file:GENSIMRECO_MuPt10_TemplateReco_'+str(opt.maxEvents)+'.root'
else:
	if opt.RECOFileName == '': opt.RECOFileName = 'file:GENSIMRECO_MuPt10_GenericReco_'+str(opt.maxEvents)+'.root'

#________________________________________________________________________
#                        Main Analysis Module

# Refitter
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

# Specify inputs/outputs
if opt.useTemplates:
	process.TrackRefitter.TTRHBuilder = 'WithAngleAndTemplate'
	if opt.outputFileName == '': opt.outputFileName = 'Ntuple_'+str(opt.maxEvents)+'.root'
else:
	process.TrackRefitter.TTRHBuilder = 'WithTrackAngle'
	if opt.outputFileName == '': opt.outputFileName = 'Ntuple_GenericReco_'+str(opt.maxEvents)+'.root'

# Load and confiugre the plugin you want to use
#---------------------------
#  PhaseIPixelNtuplizer
#---------------------------
process.PhaseINtuplizerPlugin = cms.EDAnalyzer("PhaseIPixelNtuplizer",
	trajectoryInput = cms.InputTag('TrackRefitter'),
	outputFileName = cms.untracked.string(opt.outputFileName),
	# Save everything for now
 	clusterSaveDownscaleFactor     = cms.untracked.int32(1),
	saveDigiTree                   = cms.untracked.bool(True),
	saveTrackTree                  = cms.untracked.bool(True),
	saveNonPropagatedExtraTrajTree = cms.untracked.bool(True),
	)
process.PhaseIPixelNtuplizer_step = cms.Path(process.PhaseINtuplizerPlugin)

# myAnalyzer Path
process.myAnalyzer_step = cms.Path(process.MeasurementTrackerEvent*process.TrackRefitter*process.PhaseINtuplizerPlugin)

#________________________________________________________________________
#                        DataBase Stuff

# Print settings
print "Using options: "
if opt.globalTag == '':
    print "  globalTag (auto:phase1_2017_realistic) = "+str(process.GlobalTag.globaltag)
else:
    if "auto:" in opt.globalTag:
	process.GlobalTag = GlobalTag(process.GlobalTag, opt.globalTag, '')
	print "  globalTag ("+opt.globalTag+") = "+str(process.GlobalTag.globaltag)
    else:
	process.GlobalTag.globaltag = opt.globalTag
	print "  globalTag (manually chosen)            = "+str(process.GlobalTag.globaltag)
print "  useTemplates                           = "+str(opt.useTemplates)
print "  saveRECO                               = "+str(opt.saveRECO)
print "  useRECO                                = "+str(opt.useRECO)
print "  RECOFileName                           = "+str(opt.RECOFileName)
print "  noMagField                             = "+str(opt.noMagField)
print "  outputFileName                         = "+str(opt.outputFileName)
print "  maxEvents                              = "+str(opt.maxEvents)
print "  useLocalLASim                          = "+str(opt.useLocalLASim)
print "  useLocalQuality                        = "+str(opt.useLocalQuality)
print "  useLocalLA                             = "+str(opt.useLocalLA)
print "  useLocalGain                           = "+str(opt.useLocalGain)
print "  useLocalGenErr                         = "+str(opt.useLocalGenErr)
print "  useLocalTemplates                      = "+str(opt.useLocalTemplates)
print "  useLocalDynIneff                       = "+str(opt.useLocalDynIneff)

dir   = 'sqlite_file:/afs/cern.ch/user/j/jkarancs/public/DB/Phase1/'
Danek = 'sqlite_file:/afs/cern.ch/user/d/dkotlins/public/CMSSW/DB/phase1/'

# Test Local DB conditions
# Quality
#Qua_db          = 'frontier://FrontierPrep/CMS_CONDITIONS'
Qua_db          = 'frontier://FrontierProd/CMS_CONDITIONS'
#Qua_db          = 'sqlite_file:../../../../../DB/phase1/SiPixelQuality_phase1_ideal.db'
#Qua_tag         = 'SiPixelQuality_phase1_ideal'
#Qua_tag         = 'SiPixelQuality_phase1_2017_v1'
Qua_tag         = 'SiPixelQuality_phase1_2017_v3' # 2017 May 23

# Gains
#Gain_db         = 'frontier://FrontierPrep/CMS_CONDITIONS'
#Gain_db         = 'frontier://FrontierProd/CMS_CONDITIONS'
#Gain_db         = Danek + 'SiPixelGainCalibration_phase1_ideal_v2.db'
#Gain_tag        = 'SiPixelGainCalibration_phase1_ideal_v2'
Gain_db         = Danek + 'SiPixelGainCalibration_phase1_mc_v2.db'
Gain_tag        = 'SiPixelGainCalibration_phase1_mc_v2'

# LA (SIM)
#LASim_db        = 'frontier://FrontierPrep/CMS_CONDITIONS'
#LASim_db        = 'frontier://FrontierProd/CMS_CONDITIONS'
# MC
#LASim_db        = Danek+'SiPixelLorentzAngleSim_phase1_mc_v1.db'
#LASim_tag       = "SiPixelLorentzAngleSim_phase1_mc_v1"
#LASim_db        = dir+'2017_02_13/SiPixelLorentzAngleSim_phase1_mc_v2.db'
#LASim_tag       = "SiPixelLorentzAngleSim_phase1_mc_v2"
# Data (DUMMY)
LASim_db        = dir+'2017_03_20/SiPixelLorentzAngleSim_phase1_2017_v1_TESTONLY.db'
LASim_tag       = "SiPixelLorentzAngleSim_phase1_2017_v1_TESTONLY"

# LA (RECO)
#LA_db           = 'frontier://FrontierPrep/CMS_CONDITIONS'
#LA_db           = 'frontier://FrontierProd/CMS_CONDITIONS'
# MC
#LA_db           = dir+'2017_02_13/SiPixelLorentzAngle_phase1_mc_v2.db'
#LA_tag          = 'SiPixelLorentzAngle_phase1_mc_v2'
# Data
LA_db           = dir+'2017_04_05/SiPixelLorentzAngle_phase1_2017_v1.db'
LA_tag          = 'SiPixelLorentzAngle_phase1_2017_v1'

# LA (Width)
#LA_Width_db     = 'frontier://FrontierPrep/CMS_CONDITIONS'
#LA_Width_db     = 'frontier://FrontierProd/CMS_CONDITIONS'
LA_Width_db     = dir+'2017_02_13/SiPixelLorentzAngle_forWidth_phase1_mc_v2.db'
LA_Width_tag    = 'SiPixelLorentzAngle_forWidth_phase1_mc_v2'

# GenErrors
if opt.noMagField:
	# 0T GenErrors
	#GenErr_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
	#GenErr_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
	# MC
	GenErr_db       = dir+'2017_04_05/SiPixelGenErrorDBObject_phase1_00T_mc_v2.db'
	GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_00T_mc_v2'
	# Data
	#GenErr_db       = dir+'2017_03_20/SiPixelGenErrorDBObject_phase1_00T_2017_v1.db'
	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_00T_2017_v1'
	
	# 0T Templates
	#Templates_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
	#Templates_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
	# MC
	Templates_db       = dir+'2017_04_05/SiPixelTemplateDBObject_phase1_00T_mc_v2.db'
	Templates_tag      = 'SiPixelTemplateDBObject_phase1_00T_mc_v2'
	# Data
	#Templates_db       = dir+'2017_03_20/SiPixelTemplateDBObject_phase1_00T_2017_v1.db'
	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_00T_2017_v1'
else:
	# 3.8T GenErrors
	GenErr_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
	#GenErr_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
	# MC
	#GenErr_db       = dir+'2017_02_13/SiPixelGenErrorDBObject_phase1_38T_mc_v2.db'
	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_mc_v2'
	# Data
	#GenErr_db       = dir+'2017_04_05/SiPixelGenErrorDBObject_phase1_38T_2017_v1.db'
	#GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_2017_v1'
	GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_2017_v6'
	
	# 3.8T Templates
	Templates_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
	#Templates_db       = 'frontier://FrontierProd/CMS_CONDITIONS'
	# MC
	#Templates_db       = dir+'2017_02_13/SiPixelTemplateDBObject_phase1_38T_mc_v2.db'
	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_mc_v2'
	# Data
	#Templates_db       = dir+'2017_04_05/SiPixelTemplateDBObject_phase1_38T_2017_v1.db'
	#Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_2017_v1'
	Templates_tag      = 'SiPixelTemplateDBObject_phase1_38T_2017_v6'

# Dynamic Inefficiency
#DynIneff_db     = 'frontier://FrontierPrep/CMS_CONDITIONS'
#DynIneff_db     = 'frontier://FrontierProd/CMS_CONDITIONS'
DynIneff_db     = 'sqlite_file:/data/jkarancs/CMSSW/PhaseI/CMSSW_9_2_2/src/DPGAnalysis-SiPixelTools/PixelDBTools/SiPixelDynamicInefficiency_L1_dcol0p8.db'
DynIneff_tag    = 'SiPixelDynamicInefficiency_L1_dcol0p8'

#LA
if opt.useLocalLASim :
	process.LASimReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleSimRcd"),
			tag = cms.string(LASim_tag))),
		connect = cms.string(LASim_db))
	process.lasimprefer = cms.ESPrefer("PoolDBESSource","LASimReader")

# Quality
if opt.useLocalQuality :
	process.QualityReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelQualityFromDbRcd'),
			tag = cms.string(Qua_tag))),
		connect = cms.string(Qua_db))
	process.es_prefer_QualityReader = cms.ESPrefer("PoolDBESSource","QualityReader")

# for reco
# LA 
if opt.useLocalLA :
	process.LAReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleRcd"),
			tag = cms.string(LA_tag))),
		connect = cms.string(LA_db))
	process.LAprefer = cms.ESPrefer("PoolDBESSource","LAReader")
	# now the forWidth LA
	process.LAWidthReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleRcd"),
			label = cms.untracked.string("forWidth"),
			tag = cms.string(LA_Width_tag))),
		connect = cms.string(LA_Width_db))
	process.LAWidthprefer = cms.ESPrefer("PoolDBESSource","LAWidthReader")

# Gain 
if opt.useLocalGain :
	process.GainsReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelGainCalibrationOfflineRcd'),
			tag = cms.string(Gain_tag))),
		connect = cms.string(Gain_db))
	process.Gainprefer = cms.ESPrefer("PoolDBESSource","GainsReader")

# GenError
if opt.useLocalGenErr :
	process.GenErrReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelGenErrorDBObjectRcd'),
			tag = cms.string(GenErr_tag))),
		connect = cms.string(GenErr_db))
	process.generrprefer = cms.ESPrefer("PoolDBESSource","GenErrReader")

# Templates
if opt.useLocalTemplates :
	process.TemplatesReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelTemplateDBObjectRcd'),
			tag = cms.string(Templates_tag))),
		connect = cms.string(Templates_db))
	if opt.noMagField:
		process.TemplatesReader.toGet = cms.VPSet(
			cms.PSet(
				label = cms.untracked.string('0T'),
				record = cms.string('SiPixelTemplateDBObjectRcd'),
				tag = cms.string(Templates_tag)
				)
			)
	process.templateprefer = cms.ESPrefer("PoolDBESSource","TemplatesReader")

# Dnyamic Inefficiency
if opt.useLocalDynIneff :
	process.DynIneffReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelDynamicInefficiencyRcd"),
			tag = cms.string(DynIneff_tag))),
		connect = cms.string(DynIneff_db))
	process.dynineffprefer = cms.ESPrefer("PoolDBESSource","DynIneffReader")


#---------------------------
#  Schedule
#---------------------------

# Modify Schedule
if opt.useRECO:
	process.schedule = cms.Schedule(process.myAnalyzer_step)
else:
	if not opt.saveRECO:
		process.schedule.remove(process.RECOSIMoutput_step)
	else:
		process.RECOSIMoutput.fileName = opt.RECOFileName
		# Additionally, save the pixel sim hits and digis too
		process.RECOSIMoutput.outputCommands.extend(('keep *_g4SimHits_*Pixel*_*','keep *_simSiPixelDigis_*_*','drop *_mix_simSiPixelDigis*_*'))
	# Remove unnecessary steps and add Analyzer in the end of the chain
	process.schedule.remove(process.endjob_step)
	process.schedule.remove(process.genfiltersummary_step)
	process.schedule.append(process.myAnalyzer_step)
# End of inserted code





















#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
