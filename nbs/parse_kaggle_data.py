# coding: utf-8

# Download data with kg download
# Unzip the training directory
# Run this file in the same directory as the training directory

from glob import glob
from random import shuffle
import os, shutil
import pprint

def log(msg):
  pprint.pprint(msg)


def build_data_tree(cat_files,dog_files,build_path):

  valid_sample_percentage = 0.1

  cats_build_path = os.path.join(build_path,'train/cats/')
  dogs_build_path = os.path.join(build_path,'train/dogs/')

  if os.path.exists(build_path):
    shutil.rmtree(build_path)

  os.makedirs(cats_build_path)
  os.makedirs(dogs_build_path)

  for f in cat_files:
    shutil.copy(f, cats_build_path)

  for f in dog_files:
    shutil.copy(f, dogs_build_path)

  valid_cat_files = get_sample(glob(os.path.join(cats_build_path,'*.*')),valid_sample_percentage)
  valid_dog_files = get_sample(glob(os.path.join(dogs_build_path,'*.*')),valid_sample_percentage)

  valid_cats_build_path = os.path.join(build_path,'valid/cats/')
  valid_dogs_build_path = os.path.join(build_path,'valid/dogs/')

  os.makedirs(valid_cats_build_path)
  os.makedirs(valid_dogs_build_path)

  for f in valid_cat_files:
    shutil.move(f, valid_cats_build_path)

  for f in valid_dog_files:
    shutil.move(f, valid_dogs_build_path)


def get_sample(array, percent):
  shuffle(array)
  split_point = int(percent * len(array))
  return array[:split_point]


def main():

  source_directory = 'kaggle/train'
  sorted_directory_name = 'vgg'
  sample_percentage = 0.05
  sample_directory_name = 'vgg_sample'

  # Make a comprehensive directory of sorted data
  cat_files = glob(os.path.join(source_directory,'cat.*'))
  dog_files = glob(os.path.join(source_directory,'dog.*'))

  build_data_tree(cat_files,dog_files,sorted_directory_name)


  # Make a sample directory for faster development
  sample_cat_files = get_sample(cat_files,sample_percentage)
  sample_dog_files = get_sample(dog_files,sample_percentage)

  build_data_tree(sample_cat_files,sample_dog_files,sample_directory_name)




if __name__ == '__main__':
  main()