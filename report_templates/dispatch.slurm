#!/bin/bash
#SBATCH --mail-user=jordan.gunn@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=2G
#SBATCH --time=0:20:00
#SBATCH --output=pi.txt

module load GCCcore/.10.2.0
module load Python/3.8.6

source ${HOME}/pi/bin/activate
export PYTHONPATH=$(python -c 'import sys; print(sys.path[-1])'):${PYTHONPATH}

python pi.py 1000000