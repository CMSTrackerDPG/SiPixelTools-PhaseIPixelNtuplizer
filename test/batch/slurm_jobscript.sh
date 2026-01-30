#!/bin/bash -e
#SBATCH --account=t3
#SBATCH --partition=standard
#SBATCH --cpus-per-task=4
#SBATCH --mem=4000
#SBATCH --time=8:00:00
#SBATCH --nodes=1

set -x
echo "------------------------------------------------------------"
echo "[`date`] Job started"
echo "------------------------------------------------------------"
DATE_START=`date +%s`

echo HOSTNAME: ${HOSTNAME}
echo HOME: ${HOME}
echo USER: ${USER}
echo X509_USER_PROXY: ${X509_USER_PROXY}
echo CMD-LINE ARGS: $@

if [[ "${job_num}" != "test" ]]; then
  SLURM_ARRAY_TASK_ID=$4
else
  SLURM_ARRAY_TASK_ID=1
fi

if [ -z ${SLURM_ARRAY_TASK_ID} ]; then
  printf "%s\n" "Environment variable \"SLURM_ARRAY_TASK_ID\" is not defined. Job will be stopped." 1>&2
  exit 1
fi

# define SLURM_JOB_NAME and SLURM_ARRAY_JOB_ID, if they are not defined already (e.g. if script is executed locally)
[ ! -z ${SLURM_JOB_NAME} ] || SLURM_JOB_NAME=$1
[ ! -z ${SLURM_ARRAY_JOB_ID} ] || SLURM_ARRAY_JOB_ID=local$(date +%y%m%d%H%M%S)

#SLURM_JOB_NAME=$1
echo SLURM_JOB_NAME: ${SLURM_JOB_NAME}
echo SLURM_JOB_ID: ${SLURM_JOB_ID}
echo SLURM_ARRAY_JOB_ID: ${SLURM_ARRAY_JOB_ID}
echo SLURM_ARRAY_TASK_ID: ${SLURM_ARRAY_TASK_ID}

#ARG parsing
cmssw=$2
USERDIR=$3
job_num=$4
dataTier=$5
globalTag=$6
executable=$7
certification=$8
input=$9

if [[ ${USERDIR} == /pnfs/* ]]; then
    (
      (! command -v scram &> /dev/null) || eval `scram unsetenv -sh`
      gfal-mkdir -p root://t3dcachedb03.psi.ch:1094/$USERDIR
      gfal-mkdir -p root://t3dcachedb03.psi.ch:1094/$USERDIR/logs
      sleep 5
    )
#mkdir -p $USERDIR
fi
echo OUTPUT_DIR: $USERDIR

# local /scratch dir to be used by the job
TMPDIR=/scratch/${USER}/slurm/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}
echo TMPDIR: ${TMPDIR}
mkdir -p ${TMPDIR}
NUM_LUMIBLOCK=${SLURM_ARRAY_TASK_ID}
cd ${TMPDIR}

source /cvmfs/cms.cern.ch/cmsset_default.sh

echo
echo "--------------------------------------------------------------------------------"
echo "--------------------------------------------------------------------------------"
echo "                          Creating JOB ["${job_num}"]"
echo

#export SCRAM_ARCH=slc7_amd64_gcc10
#export SCRAM_ARCH=slc7_amd64_gcc820
export SCRAM_ARCH=el9_amd64_gcc12
cd ${TMPDIR}

scramv1 project CMSSW ${cmssw}
cd ${cmssw}/src
eval `scram runtime -sh`
git clone https://github.com/CMSTrackerDPG/SiPixelTools-PhaseIPixelNtuplizer SiPixelTools/PhaseIPixelNtuplizer
cd SiPixelTools/PhaseIPixelNtuplizer

# output file
output="Ntuple_"${job_num}".root"

echo
echo "--------------------------------------------------------------------------------"
echo "                                JOB ["${job_num}"] ready"
echo "                                    Compiling..."
echo

VER=$(echo $CMSSW_VERSION | sed "s:CMSSW::g" | sed "s:\_::g" | cut -c 1-3)
scram b -j 8 USER_CXXFLAGS="-DCMSSW_VERSION=$VER"

echo
echo "--------------------------------------------------------------------------------"
echo "                                 Compiling ready"
echo "                               Starting JOB ["${job_num}"]"
echo

#file management
if [ ${certification} != "DUMMY" ];then
    cp ${certification} .      #copy the GoodLumi.json list to working directory
fi
cp ${executable} . 
cat ${input} | sed "s;^;root://cms-xrd-global.cern.ch:/;" > tmp.sh
cat tmp.sh
chmod 755 tmp.sh  

executable=`ls -l | grep .py | grep run_PhaseIPixelNtuplizer | awk '{print $NF}'`
echo $executable
files=`cat tmp.sh | grep .root | awk '{print $NF}' | sed "s;^;file:;" | tr "\n" "," | sed "s:,:\", \":g" | sed 's/.\{3\}$//' | sed 's:^:\":' | sed 's:\":\":g'`
echo $files
sed -e "s;___EXCHANGE___FILES___;${files};g" ${executable} > tmp

cat tmp
json=`ls -l | grep .json | awk '{print $NF}'`
if [ ${certification} != "DUMMY" ];then
    sed -e "s;___EXCHANGE___CERTJSON___;${json};g" tmp > ${executable}
else
    mv tmp ${executable}
fi
chmod 755 ${executable}
cp ${executable} /work/${USER}

if [[ $# > 9 ]]; then
    echo $#
    echo "cmsRun ${executable} globalTag=${globalTag} dataTier=${dataTier} inputFileName=${input} outputFileName=$output maxEvents=$9\n"
    cmsRun ${executable} dataTier=${dataTier}  globalTag=${globalTag} outputFileName=$output maxEvents=${10} 
else
    echo "cmsRun ${executable} globalTag=${globalTag} dataTier=${dataTier} inputFileName=${input} outputFileName=$output maxEvents=-1\n"
    cmsRun ${executable} dataTier=${dataTier}  globalTag=${globalTag} outputFileName=$output maxEvents=-1
fi


echo
echo "--------------------------------------------------------------------------------"
echo "                               JOB ["${job_num}"] Finished"
echo "                              Writing output to EOS?..."
echo

# Copy to Eos
if [[ ${USERDIR} == /pnfs/* ]]; then
    xrdcp -f -N $output root://t3dcachedb03.psi.ch:1094//$USERDIR/$output
    xrdcp -f -N /work/${USER}/test/.slurm/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.out root://t3dcachedb03.psi.ch:1094//$USERDIR/logs/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.out
    xrdcp -f -N /work/${USER}/test/.slurm/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.err root://t3dcachedb03.psi.ch:1094//$USERDIR/logs/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.err
else
    cp $output $USERDIR/$output
    cp  /work/${USER}/test/.slurm/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.out $USERDIR/logs/${SLURM_JOB_ID}_${SLURM_JOB_ID}_${4}.out
    cp  /work/${USER}/test/.slurm/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${4}.err $USERDIR/logs/${SLURM_JOB_ID}_${SLURM_JOB_ID}_${4}.err
fi

echo
echo "Output: "
ls -l $USERDIR/$output

cd ../../../..
rm -rf $2
cd ..
rm -r ${SLURM_JOB_NAME}_${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}
echo
echo "--------------------------------------------------------------------------------"
echo "                                 JOB ["${job_num}"] DONE"
echo "--------------------------------------------------------------------------------"
echo "--------------------------------------------------------------------------------"
