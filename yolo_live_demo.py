#
# YOLO5 live done by Jan Zbirovsky
#
# 
# YOLO5 credit: https://github.com/ultralytics/ultralytics

import cv2
import random
from PIL import Image
import matplotlib.pyplot as plt
#from ultralytics import YOLO

import torch
from torchvision.transforms import functional as F

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# show size of webcam frame
SIZE_PCT = 170

# function to resize webcam frame
def resize_frame(frame, SIZE_PCT):
    
    width = int(frame.shape[1] * SIZE_PCT / 100)
    height = int(frame.shape[0] * SIZE_PCT / 100)
    dim = (width, height)
  
    # resize image
    return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

# define path to our model, then load it
path = r'./model/pretrained_bosch_model.pt'
model = torch.hub.load('ultralytics/yolov5', 
                       'custom', 
                       path=path)

# webcam init
cap = cv2.VideoCapture(0)

# Check if the camera is successfully connected
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# tuples of colors
# we have just three classes
classes_colors = (
        (50, 220, 20),  # Bosch
        (50, 20, 220),  # Digi@JhP
        (220, 50, 20)   # Eye
)

# Read frames from the camera until the user quits
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not captured successfully, break the loop
    if not ret:
        print("Failed to capture frame")
        break

    # Run inference on the source
    results = model(frame)

    # get bounding boxes
    boxes = results.xyxy[0].numpy()
    labels = results.names[0]

    # Visualize the results on the frame
    annotated_frame = frame.copy()

    for idx, box in enumerate(boxes):
        
        # get bounding box details
        x1, y1, x2, y2, conf, class_number = box
        
        if int(class_number)<(len(classes_colors)) and conf > 0.3:
            cv2.rectangle(annotated_frame, (int(x1), int(y1)), (int(x2), int(y2)), classes_colors[int(class_number)], 2)
            
            # text
            if int(class_number) == 0:
                text = 'BOSCH'
            elif int(class_number) == 1:
                text = 'DIGI@JhP'
            elif int(class_number) == 2:
                text = 'OKO'    

            # font 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            
            # org 
            org = (int(x1), int(y1-10))
            
            # fontScale 
            fontScale = 1
            
            # Blue color in BGR 
            color = classes_colors[int(class_number)]
            
            # Line thickness of 2 px 
            thickness = 2
            
            # print class name
            cv2.putText(annotated_frame, text + " (" + format(conf, ".2f") + ")", org, font, fontScale, color, thickness, cv2.LINE_AA)

    # demo by
    cv2.putText(annotated_frame, "Made by Jan Zbirovsky", org=(5, 10), fontFace=font, fontScale=fontScale * .5, color=(50, 240, 50), thickness=int(thickness * .5), lineType=cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Camera', resize_frame(annotated_frame, SIZE_PCT))
    
    # Wait for the user to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close any open windows
cap.release()
cv2.destroyAllWindows()
print("Resources released")
