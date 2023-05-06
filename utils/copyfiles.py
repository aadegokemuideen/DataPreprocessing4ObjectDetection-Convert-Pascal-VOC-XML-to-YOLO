'''
It help to copy the exitings images and
annottations into new folders
'''

import os
import shutil

def copyfiles(fil, root_dir, image_dir,label_dir):
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    #image
    src = fil # source
    dest = os.path.join(root_dir,image_dir, f"{filename}.jpg")
    shutil.copyfile(src,dest)

    # label
    src = os.path.join(label_dir, f"{filename}.txt")
    dest = os.path.join(root_dir, label_dir, f"{filename}.txt")
    if os.path.exists(src):
        shutil.copyfile(src, dest)




