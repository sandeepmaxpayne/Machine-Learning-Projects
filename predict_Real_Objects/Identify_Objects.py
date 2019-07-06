# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:15:26 2019

@author: Sandeep
"""

############################################################ ARGUMENT PARSER ########################################################################333

#python <filename.py> --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel --image images1/example1.jpg
import numpy as np
import argparse
import cv2

#opencv help to see
#convulation network is to predict and to process it
#construct argparse
ap = argparse.ArgumentParser()
ap.add_argument("-1", "--image", required=True, help = "path to input image")
ap.add_argument("-p", "--prototxt", required=True, help="path to Cafe 'deploy' prototype file")
ap.add_argument("-n", "--model", required=True, help="path to Cafe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability  to filter weak")
                

args = vars(ap.parse_args())

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat" ,"chair", "cow", "diningtable", "dog", "horse",
           "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

COLOR = np.random.uniform(0, 255, size=(len(CLASSES), 3)) # 0->low value, 255->high value, d_type: 1->Int, 2->Float, 3->String

#Loading our CNN model
print("[INFO] loading model ..........") 
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"]) # similar to model.compile

#####Note : Normalization is done by the author of the MoblieNet SSD

image = cv2.imread(args["image"]) # image recieved from command line, resiging image by 300 X 300 px
(h,w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 0.007843, (300,300), 127.5) #127.5 is crop size , size(300 X 300)

net.setInput(blob) #Load input image and construct a input blob for the image
detections = net.forward()

for i in np.arange(0, detections.shape[2]):
    # extract the confidence
    # prediction
    confidence = detections[0, 0, i, 2]

    #filter out the weak detections
    #greater than the minimum confidence
    if (confidence > args["confidence"]):
        # extract the index of the class label detection
        # then conpute the (x,y) coordinates of the boomering box

        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startx, starty, endx, endy) = box.astype("int")

        #display the prediction

        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[Info]{}".format(label))
        cv2.rectangle(image, (startx, starty), (endx, endy), COLOR[idx], 2)
        y = starty - 15 if starty - 15 > 15 else starty + 15
        cv2.putText(image, label, (startx, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR[idx], 2)

cv2.imshow("Output", image)
cv2.waitKey(0)
