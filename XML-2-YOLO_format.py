'''
Tips and tricks to preprocess image datasets

PASACAL VOC XML to YOLO File format for Object 
Detection

VOC = Visual Object Classes

It cover the following steps
- convert XML annotations to YOLO annotations
- visualize the bounding boxes in images using
the newly created YOLO annotations
- split the datasest into train, validation and test
set

One of the major problem with PASCAL VOC XML annotations is that 
we cannot use it directly for training 
especially on object detection tasks
Most of the state-of-the-art models rely on different
annotations formats. The most popular are.

-COCO- a single Json file consists of five sectons of
informations for the entire datasets
-YOLO- individuals text file per images with the same
entire datasets

YOLO:
The specifications for YOLO are as follows

- each object should have its own row in the text file
- each row should have the following pattern
-- class x-centre y-centre width height
-class number must be a integer and atrts from o
-x-center, y-center, width, height must be in normalized form
(range 0 to 1)


'''

import xml.etree.ElementTree as ET
import glob
import os
import json
from utils.convert_bbox_from_one_form_2_other import *


classes  = []
input_dir = "annotations/"
output_dir = "labels/"
image_dir = "images/"

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)


# Get XML Files
files = glob.glob(os.path.join(input_dir, "*.xml"))
for fil in files:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]
    #fileInpath = [os.path.join(image_dir, f'{filename}.png'), os.path.join(image_dir, f'{filename}.jpg')]
    #if not os.path.exits(file_in_path for file_in_path in fileInpath):
    if not ( os.path.exists(os.path.join(image_dir,f'{filename}.png'))  \
       or  os.path.exists(os.path.join(image_dir, f'{filename}.jpg')) ):
        print(f"{filename} images does not exits!")
        continue
    #the code above will print out the name of the annotated images
    # that is without its image pair. Either delete the annotations
    # fill in the missing images

    # Let parse the content of XML Files
    # we are using ET module to parse the content of the 
    # XML files
    result = []
    tree =ET.parse(fil)
    root = tree.getroot()
    width = int(root.find("size").find("width").text)
    height = int(root.find("size").find("height").text)

    for obj in root.findall("object"):
        label  = obj.find("name").text
        if label not in classes:
            classes.append(label)
        index = classes.index(label)
        #print(index)
        pil_bbox = [int(x.text) for x in obj.find("bndbox")]
        yolo_bbox = xml_to_yolo_bbox(pil_bbox,width, height)
        bbox_string = " ".join([str(x) for x in yolo_bbox])
        result.append(f"{index} {bbox_string}")
        #print(result)

    if result:
        # generate a yolo format text 
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(result))

'''
Note that new labels will be automatically added into the classes variable
The index is based on the first occurrence of the corresponding labels. As a
result, we  should save the classes variable as a text file for reference

'''

with open("classes.txt", "w", encoding = "utf8") as f:
    f.write(json.dumps(classes))

'''
It will generate a text file called classes.txt
The text file will contain a list of strings representing
all the unique classes in the datasets
'''








