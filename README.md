# Download the RL Unplugged Atari (ordered) dataset

To download the [Atari dataset](https://www.tensorflow.org/datasets/catalog/rlu_atari_checkpoints_ordered) there are a few extra dependencies. The minimum amount of such dependencies was registered in `requirements.txt`.

To download all the games and runs from this dataset, we only need to run `DL.sh` which will launch 46 games * 5 games = 230 jobs to download the whole dataset. Each game/run combination is about 75Gb, for a total of 17Tb.

This script expects that a `virtualenv` exists (written as RLU_ENV in this example) with the dependencies listed in `requirements.txt`. The directory to download the dataset to can be specific as an argument:

```
bash DL.sh directory_for_dataset
```
