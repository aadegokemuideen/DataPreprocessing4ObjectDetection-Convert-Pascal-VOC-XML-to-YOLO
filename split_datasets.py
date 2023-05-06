"""

In this part, we split the data into three different portions
namely:

train
Validation 
test

"""

import random
import glob
import os 
import shutil
from utils.copyfiles import copyfiles

label_dir = "labels/"
image_dir = "images/"
lower_limit = 0
files = glob.glob(os.path.join(image_dir, "*.jpg"))

'''
glob is used on images file instead of annotations
because there can be cases where an images contain no label
.DO not be surprised if the total number of images
does not match with the total number of label files
'''

random.shuffle(files)
'''
Note that the final split for all the three protions will
be different on each run. This can be an issue if the datasets
is imbalance. Modify the script accordingly
train: 80% of the datasest
val: 10% of the datasets
test: 10% of the datasets
'''

folders = {"train": 0.2, "val": 0.2, "test": 0.6}
check_sum = sum([folders[x] for x in folders])

assert check_sum == 1.0, "Split proportion is not equal to 1.0"

#let copyfiles
for folder in folders:
    os.mkdir(folder)
    temp_label_dir = os.path.join(folder,label_dir) # create director and folder to put label
    os.mkdir(temp_label_dir)
    temp_image_dir = os.path.join(folder,image_dir)
    os.mkdir(temp_image_dir) # create directory and folder to put image

    limit = round(len(files) * folders[folder]) # no of train/val/test images to take from a to point b
    for fil in files[lower_limit:lower_limit + limit]:
        copyfiles(fil, folder, image_dir, label_dir)
        lower_limit = lower_limit + limit
        #print(files[lower_limit:lower_limit + limit])
