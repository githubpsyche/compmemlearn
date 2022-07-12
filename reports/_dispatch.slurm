#!/bin/bash
#SBATCH --mail-user=jordan.gunn@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --time=20:00:00

module load GCCcore/.10.2.0
module load Python/3.8.6

source ${HOME}/compmemlearn/bin/activate
export PYTHONPATH=$(python -c 'import sys; print(sys.path[-1])'):${PYTHONPATH}

echo ${PARAMETER_SCRIPT}
python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}"