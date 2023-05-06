'''
Visualizing the Bounding Boxes
In this case we can use ither the Pillow or OpenCV pakages
for it. This tutorial uses the Pillow packages to darw the bounding boxes
'''

# from PIL import Image, ImageDraw
import cv2
from utils.convert_bbox_from_one_form_2_other import *
import os
import imutils


def draw_image(img, bboxes, index_per_boxes):
    # draw = ImageDraw.Draw(img)
    for i, (bbox, index) in enumerate(zip(bboxes, index_per_boxes)):
        # draw.rectangle(bbox, outline="red", width=2)
        #green = (0, 255, 0)  # BGR
        color = [(0, 255, 0), (255, 0, 0), (0, 0, 255),
                 (200, 100, 110), (10, 11, 150), (230, 120, 150)] # if no of classes increases, then increase color types

        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color[int(index[0])], 3)

    img = imutils.resize(img, height=500)  # resize the images
    # img.show()
    cv2.imshow("img", img)


baseImagedir = "images/"
baseLabeldir = "labels/"
image_filenames = os.listdir(baseImagedir)
label_filenames = os.listdir(baseLabeldir)


print(image_filenames)


for image_filename, label_filename in zip(image_filenames, label_filenames):
    bboxes = []
    index_per_boxes = []
    # img = Image.open(os.path.join(baseImagedir, image_filename))
    img = cv2.imread(os.path.join(baseImagedir, image_filename))
    # print(img, img.shape)
    height, width = img.shape[:2]
    with open(os.path.join(baseLabeldir, label_filename), "r", encoding="utf8") as f:
        for line in f:
            data = line.strip().split(' ')
            bbox = [float(x) for x in data[1:]]
            bboxes.append(yolo_to_xml_bbox(bbox, width, height)) # bbox = xmin, ymin,xmax, ymax that is XML
            index = [float(x) for x in data[:1]]
            index_per_boxes.append(index) ## This will assist me to select the same color for the same class

            # print(bbox,bboxes)
            # resized = imutils2.resize(image, height=150)
        #print(index_per_boxes)
        draw_image(img, bboxes, index_per_boxes)
        cv2.waitKey(0)
    
