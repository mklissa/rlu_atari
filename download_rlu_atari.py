"""A scritp to download RLU Atari datasets."""

import argparse
import rlds
import tensorflow_datasets as tfds


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--game",  type=str,
      help="Atari game to download.", default="Alien")
  parser.add_argument("--run", type=int,
      help="Which run from the game to download. (goes from 1 to 5)")
  parser.add_argument("--download_dir", type=str,
      help="Where to donwload the directory to.")
  args = parser.parse_args()
  return args


def download_dataset(
    game,
    run,
    download_directory,
    version = ':1.1.0',
):
  """Create Atari dataset.

  Reference: https://github.com/google-research/rlds

  Args:
    game: AtariGame, game to create split from.
    run: int, specific run to create dataset from.
    download_directory: the directory to downlaod the dataset to.
    version: str, dataset version.
  """
  dataset_name = f'rlu_atari_checkpoints_ordered/{game}_run_{run}{version}'
  builder = tfds.builder(dataset_name)

  splits = []

  for split_name, info in builder.info.splits.items():
    num_episodes = int(1.0 * info.num_examples)
    if num_episodes == 0:
      raise ValueError(
          f'{data_proportion_per_checkpoint*100.0}% leads to 0 '
          f'episodes in {split_name}!'
      )
    # Sample first `data_percent` episodes from each of the data split
    splits.append(f'{split_name}[:{num_episodes}]')

  read_config = tfds.ReadConfig(
      interleave_cycle_length=len(splits),
      shuffle_reshuffle_each_iteration=True,
      enable_ordering_guard=False,
  )

  # Will download the dataset here
  tfds.load(
      dataset_name,
      data_dir=download_directory,
      split='+'.join(splits),
      read_config=read_config,
      shuffle_files=True,
  )


if __name__ == "__main__":
  args = parse_args()

  download_dataset(
          game=args.game, run=args.run, download_directory=args.download_dir)
