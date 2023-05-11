#!/usr/bin/env bash

seeds=($(seq 1 1 5))
envnames="BeamRider DemonAttack DoubleDunk IceHockey MsPacman Pooyan RoadRunner Robotank Zaxxon Alien Amidar Asterix Assault Atlantis BattleZone BankHeist Boxing Breakout Carnival Centipede ChopperCommand CrazyClimber Enduro FishingDerby Freeway Frostbite Gopher Gravitar Hero Jamesbond Kangaroo KungFuMaster Krull NameThisGame Phoenix Pong Qbert Riverraid Seaquest SpaceInvaders StarGunner TimePilot UpNDown VideoPinball WizardOfWor YarsRevenge"

for envname in ${envnames[@]}
do
    for seed in ${seeds[@]}
    do
        if [ -f temprun.sh ] ; then
            rm temprun.sh
        fi
        echo "#!/bin/bash" >> temprun.sh
        echo "#SBATCH --output=/tmp/${envname}_seed${seed}_%j.out" >> temprun.sh
        echo "#SBATCH --job-name=${envname}_seed${seed}_%j" >> temprun.sh
        echo "#SBATCH --nodes=1" >> temprun.sh
        echo "#SBATCH --ntasks=1" >> temprun.sh
        echo "#SBATCH --cpus-per-task=4" >> temprun.sh
        echo "#SBATCH --mem=40G" >> temprun.sh
        echo "#SBATCH --time=2:55:00" >> temprun.sh
        echo "module load python/3.8" >> temprun.sh
        echo "source RLU_ENV/bin/activate" >> temprun.sh
        echo "cd $HOME/scratch/rlu_atari/" >> temprun.sh
        k="python download_rlu_atari.py --run $seed --game $envname"
        echo $k >> temprun.sh
        echo $k
        eval "sbatch temprun.sh"
        rm temprun.sh
    done
