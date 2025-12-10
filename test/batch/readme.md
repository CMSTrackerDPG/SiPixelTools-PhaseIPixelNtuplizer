# Automated Batch Submission of **SiPixelTools PhaseIPixelNtuplizer** on PSI Tier-3 (SLURM)

This README describes the workflow used to automate batch job submission of the **PhaseIPixelNtuplizer** on the **PSI Tier-3** cluster using **SLURM**.  
Generally, the PhaseIPixelNtuplizer produces ntuples that serve as input to the **PixelHistoMaker**, which analyzes pixel detector data and produces monitoring plots such as trend plots.

Details of the Ntuplizer itself are provided in the PixelNtuplizer [README](https://github.com/CMSTrackerDPG/SiPixelTools-PhaseIPixelNtuplizer/blob/master/README.md).  
**This document focuses solely on the automated submission workflow used for processing *2025 data*.** It is *not* a full description of all script features.

## The workflow

### 1. Locate the Input Data in DAS

Ensure the relevant datasets exist. Query DAS with:
```
dataset=/Muon*/Run2025SiPixelTight*/ALCARECO
```
The relevant streams are `Muon0` and `Muon1`, which are exclusive datastreams—both must be processed.