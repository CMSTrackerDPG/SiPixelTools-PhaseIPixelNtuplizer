# Workflow for Automated Batch Submission on PSI Tier-3 with SLURM

This README describes the workflow used to automate batch job submission of the **PhaseIPixelNtuplizer** on the **PSI Tier-3** cluster using **SLURM**.  
Generally, the PhaseIPixelNtuplizer produces ntuples that serve as input to the **PixelHistoMaker**, which analyzes pixel detector data and produces monitoring plots such as trend plots.

Details of the Ntuplizer itself are provided in the PixelNtuplizer [README](https://github.com/CMSTrackerDPG/SiPixelTools-PhaseIPixelNtuplizer/blob/master/README.md).  
**This document focuses only on the submission workflow used for processing *2025 data*.** It is *not* a full description of all script features.

## The workflow

### 1. Locate the Input Data in DAS

Ensure the relevant datasets exist. Query DAS with:
```
dataset=/Muon*/Run2025SiPixelTight*/ALCARECO
```
The relevant streams are `Muon0` and `Muon1`, which are exclusive datastreams—both must be processed.


---

### 2. Obtain and Prepare the Golden JSON

Download the certified golden JSON for the relevant 2025 era:

https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions25/

Some manual adjustments may be required so that the JSON includes only the run ranges present in the dataset being processed.

---

### 3. Update the Configuration JSON (e.g., `Muon0_Run2024F_Tight.json`)

Modify the configuration JSON for the chosen era:

| Field | Description |
|-------|-------------|
| **taskname** | Should clearly indicate the era (e.g., `Muon0_Run2025D_Tight`). |
| **job_template** | Usually `"slurm_jobscript.sh"`. |
| **sample** | Update to the correct dataset for the era |
| **outdir** | Directory where the generated ntuples will be stored |
| **cmsRun_script** | Path to the CMSSW config created earlier (by following instructions on [README](https://github.com/CMSTrackerDPG/SiPixelTools-PhaseIPixelNtuplizer/blob/master/README.md)) |
| **cmssw** | CMSSW release to run with (check in **DAS → Configs**) |
| **conditions** | GlobalTag for the era (from **DAS → Configs**) |
| **cert** | Path to the prepared golden JSON certification in step 2|

---

### 4. Create the Job Structure

This step requires a valid VOMS proxy: `voms-proxy-init -voms cms -valid 168:00`

Then, by running:
```
python my_batch_sub_script.py --input Muon0_Run2024F_Tight.json --create
```
This will:

- Create a task directory (named from `taskname` above)
- Query DAS for files matching each run number
- Generate **one job per run**
- Create submission scripts:
  - `alljobs.sh` (submit all jobs)
  - `test.sh` (submit a single job)
- Copy the certification JSON and job template into the task directory
- Prompt for immediate submission (`y / n / test`)


#### The task directory structure 
```
taskname/
├── filelists/
│   ├── input_run123456.txt
│   ├── input_run123457.txt
│   └── job_list.txt
├── slurm_jobscript.sh
├── Cert_Collisions2024_eraX_JSON.txt
├── alljobs.sh
├── test.sh
└── summary.txt
```

---

### 5. Submitting the jobs

By prompting `y`, all the jobs for all runs are immediately submitted.

If `n` is chosen, the runs can be submitted later by running:
```
python my_batch_sub_script.py --input Muon0_Run2024F_Tight.json --submit
```

The log output directory is defined inside `slurm_jobscript.sh`.

 *Troubleshooting:* If access issues occur when reading data from remote sites, transferring the necessary input datasets locally to T3 resolves the problem.

---

### 6. Monitoring Job Status

Check job progress with:
```
python my_batch_sub_script.py --input Muon0_Run2024F_Tight.json --status
```

The script reports:

- **Pending (PD)** jobs  
- **Running (R)** jobs  
- **Done** (STDOUT log exists)  
- **Completed** (output ROOT file exists)

If the number of Jobs and Completed matches, ntuple production was successful.

---

### 7. Output

The workflow produces:

- **One ROOT file per run**, written to the directory specified in `outdir`. Each file is named `Ntuple_XXXX.root`, where `XXXX` is the job number.

