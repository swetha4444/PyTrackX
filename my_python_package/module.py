from .detection import detect_boundary
from scipy.spatial import distance as dist
from .config import camera_no
import matplotlib.pyplot as plt
import pandas as pd
from .config import MIN_CONF,confidence_threshold
from track import *
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import time
import cv2

# YOLO Object tracking (yolo-folder-path,video,object): string,string,string

def track_object(yolo_path,video_path,object):
    #Labels defined
    centroids_result = []
    labelsPath = yolo_path+"coco.names"
    LABELS = open(labelsPath).read().strip().split("\n")

    #Colours defined
    COLORS = np.random.randint(0,
                            255,
                            size=(len(LABELS), 3),
                            dtype="uint8")

    #YOLO algo imported
    weightsPath = yolo_path+"yolov3.weights"
    configPath = yolo_path+"yolov3.cfg"
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

    tracker = EuclideanDistTracker()
    cap = cv2.VideoCapture(video_path)       #Start Video Capturing

    while(cap.isOpened()):
        flag,frame = cap.read()
        f_width = cap.get(3)
        f_height = cap.get(4)
        
        if (flag == False):
            break

        frame = cv2.resize(frame, (720, 640))
        (H,W) = frame.shape[:2]
        
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()] #Output layer names


        #* PREDICTING PEOPLE
        #Processing the frame
        blob = cv2.dnn.blobFromImage(frame,
                                    1/255.0,
                                    (416, 416),
                                    swapRB=True,
                                    crop=False)

        results,boxes,idxs,dets,centroids = detect_boundary(frame, net, ln, MIN_CONF, personIdx=LABELS.index(object))
        boxes_ids,center = tracker.update(boxes)
        centroids_result.append(center)
        
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()
        print("Time taken to predict the image: {:.6f}seconds".format(end-start))

        color = (0, 0, 255)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
            text = "Player "
            cv2.putText(frame, text+str(id), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        cv2.imshow("Image",frame)
        if cv2.waitKey(75) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    f = open(object+"coords.txt", "a")
    f.write(centroids_result)
    f.write("WIDTH: "+f_width)
    f.write("HEIGHT: "+f_height)
    f.close()