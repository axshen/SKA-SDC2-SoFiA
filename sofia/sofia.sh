#!/bin/bash

#SBATCH --job-name=sofia
#SBATCH --output=sofia_output_%j.log
#SBATCH --error=sofia_error_%j.log
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --mem=27G

sofia $1
