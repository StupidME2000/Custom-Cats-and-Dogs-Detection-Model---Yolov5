import argparse
import os
import sys
import shutil
import random
from pathlib import Path

# Define and parse user input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--datapath', help='Path to data folder containing image and annotation files', required=True)
parser.add_argument('--train_pct', help='Ratio of images to go to train folder; the rest go to validation folder (example: ".8")', default=0.8, type=float)

args = parser.parse_args()

data_path = args.datapath
train_percent = args.train_pct

# Check for valid entries
if not os.path.isdir(data_path):
    print('Directory specified by --datapath not found. Verify the path is correct and try again.')
    sys.exit(0)
if not (0.01 <= train_percent <= 0.99):
    print('Invalid entry for train_pct. Please enter a number between 0.01 and 0.99.')
    sys.exit(0)

val_percent = 1 - train_percent

# Define paths to image and annotation folders
input_image_path = os.path.join(data_path, 'images')
input_label_path = os.path.join(data_path, 'labels')

# Define paths to data directory, train and validation datasets
data_dir = os.path.join(os.getcwd(), 'data')
train_img_path = os.path.join(data_dir, 'train/images')
train_txt_path = os.path.join(data_dir, 'train/labels')
val_img_path = os.path.join(data_dir, 'validation/images')
val_txt_path = os.path.join(data_dir, 'validation/labels')

# Create folders if they don't already exist
for dir_path in [train_img_path, train_txt_path, val_img_path, val_txt_path]:
    os.makedirs(dir_path, exist_ok=True)
    print(f'Created folder at {dir_path}.')

# Get list of all images and annotation files
img_file_list = list(Path(input_image_path).rglob('*'))
txt_file_list = list(Path(input_label_path).rglob('*'))

print(f'Number of image files: {len(img_file_list)}')
print(f'Number of annotation files: {len(txt_file_list)}')

# Determine number of files to move to each folder
train_num = int(len(img_file_list) * train_percent)
val_num = len(img_file_list) - train_num

print(f'Images moving to train: {train_num}')
print(f'Images moving to validation: {val_num}')

# Select files randomly and copy them to train or validation folders
for i, set_num in enumerate([train_num, val_num]):
    for _ in range(set_num):
        img_path = random.choice(img_file_list)
        img_fn = img_path.name
        base_fn = img_path.stem
        txt_fn = base_fn + '.txt'
        txt_path = os.path.join(input_label_path, txt_fn)

        new_img_path = train_img_path if i == 0 else val_img_path
        new_txt_path = train_txt_path if i == 0 else val_txt_path

        shutil.copy(img_path, os.path.join(new_img_path, img_fn))
        if os.path.exists(txt_path):
            shutil.copy(txt_path, os.path.join(new_txt_path, txt_fn))
        
        img_file_list.remove(img_path)
