#!/bin/bash

DISPATCH_PATH='reports/_dispatch.slurm'
TARGET_PATH='C:/Users/gunnj/compmemlearn/projects/instance_cmr/'
PARAMETER_SCRIPT='C:/Users/gunnj/compmemlearn/reports/subjectwise_model_evaluation/_dual_store_parametrize'

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}"  "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahana2014'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahanaCond1'
TRIAL_FILTER='condition == 1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahanaCond4'
TRIAL_FILTER='condition == 4'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HealyKahana2014.csv'
SECTION_TAG='HealyKahana2014'
TRIAL_FILTER='task == -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HowardKahana2005.csv'
SECTION_TAG='HowardKahana2005'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HowardKahana2005.csv'
SECTION_TAG='HowardKahana2005Cond1'
TRIAL_FILTER='condition == 1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_LL20'
TRIAL_FILTER='`list length` == 20'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_NOT_LL20'
TRIAL_FILTER='`list length` != 20'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &


DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_LL40'
TRIAL_FILTER='`list length` == 40'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_NOT_LL40'
TRIAL_FILTER='`list length` != 40'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &




DISPATCH_PATH='reports/_dispatch.slurm'
PARAMETER_SCRIPT='reports/subjectwise_model_evaluation/_single_store_parametrize'

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahana2014'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahanaCond1'
TRIAL_FILTER='condition == 1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/LohnasKahana2014.csv'
SECTION_TAG='LohnasKahanaCond4'
TRIAL_FILTER='condition == 4'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HealyKahana2014.csv'
SECTION_TAG='HealyKahana2014'
TRIAL_FILTER='task == -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HowardKahana2005.csv'
SECTION_TAG='HowardKahana2005'
TRIAL_FILTER='subject > -1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/HowardKahana2005.csv'
SECTION_TAG='HowardKahana2005Cond1'
TRIAL_FILTER='condition == 1'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_LL20'
TRIAL_FILTER='`list length` == 20'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_NOT_LL20'
TRIAL_FILTER='`list length` != 20'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &


DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_LL40'
TRIAL_FILTER='`list length` == 40'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &

DATA_PATH='../../data/Murdock1962.csv'
SECTION_TAG='Murdock1962_NOT_LL40'
TRIAL_FILTER='`list length` != 40'

sbatch --job-name="${SECTION_TAG}_${PARAMETER_SCRIPT}.run" --output="${PARAMETER_SCRIPT}_${SECTION_TAG}.out" --export=ALL,PARAMETER_SCRIPT="${PARAMETER_SCRIPT}",DATA_PATH="${DATA_PATH}",TRIAL_FILTER="${TRIAL_FILTER}",SECTION_TAG="${SECTION_TAG}",TARGET_PATH="${TARGET_PATH}" ${DISPATCH_PATH}
nohup python ${PARAMETER_SCRIPT}.py "${DATA_PATH}" "${TRIAL_FILTER}" "${SECTION_TAG}" "${TARGET_PATH}" > "${PARAMETER_SCRIPT}_${SECTION_TAG}.out" 2>&1 &
