'''
-xml-2-yolo-bbox: convert XML bounding box (xmin, ymin, xmax, ymax)
to YOLO bounding box (x-center, y-center, width, height)

-yolo-2-xml-bbox: convert YOLO bounding boxes to XML bounding box

'''

def xml_to_yolo_bbox(bbox, w, h):
    # bbox: xmin, ymin, xmax, ymax
    x_center = ((bbox[2] + bbox[0]) / 2 ) / w # find the center and sacle by w fo  normalization 
    y_center = ((bbox[3] + bbox[1]) / 2 ) / h
    width = (bbox[2] - bbox[0]) / w
    height =  (bbox[3] - bbox[1]) / h

    return [x_center, y_center, width, height]


def yolo_to_xml_bbox(bbox, w, h):
    # bbox: x_center, y_center, width, height
    w_half_len =(bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)

    return [xmin, ymin, xmax, ymax]
