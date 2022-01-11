from .detection import detect_boundary
from scipy.spatial import distance as dist
from .config import camera_no
import matplotlib.pyplot as plt
import pandas as pd
from .config import MIN_CONF,confidence_threshold
from .track import *
import numpy as np
import time
import cv2
import mediapipe as mp

# YOLO Object tracking (yolo-folder-path,video,object): string,string,string
def track_object(yolo_path,video_path,object,min_conf=MIN_CONF):
    #Labels defined
    centroids_result = []
    labelsPath = yolo_path+"/coco.names"
    LABELS = open(labelsPath).read().strip().split("\n")

    #Colours defined
    COLORS = np.random.randint(0,
                            255,
                            size=(len(LABELS), 3),
                            dtype="uint8")

    #YOLO algo imported
    weightsPath = yolo_path+"/yolov3.weights"
    configPath = yolo_path+"/yolov3.cfg"
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

        results,boxes,idxs,dets,centroids = detect_boundary(frame, net, ln, min_conf, personIdx=LABELS.index(object))
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
            text = object+" "
            cv2.putText(frame, text+str(id), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        cv2.imshow("Image",frame)
        if cv2.waitKey(75) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    f = open(object+"_coords.txt", "a")
    for center in centroids_result:
        f.write(str(center)+"\n")
    f.write("WIDTH: "+str(f_width))
    f.write("\nHEIGHT: "+str(f_height))
    f.close()


# Mediapipe Posture tracking (width,height,video_path,min_dconf,min_tconf): int,int,string/int(0),float,float
# video_path (0-live webcam capture, path[string]-video input feed path)

def track_posture(WIDTH=600,HEIGHT=600,video_path=0,min_dconf=0.5,min_tconf=0.5):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    f = open("posture_coords.txt", "a")
    capture = cv2.VideoCapture(video_path)
    with mp_pose.Pose(min_detection_confidence=min_dconf,min_tracking_confidence=min_tconf) as pose :
        while(capture.isOpened()) :
            ret , frame = capture.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            result = pose.process(image)

            try :
                landmarks = result.pose_landmarks.landmark
                coordinates = {"Nose" : [WIDTH *landmarks[0].x,HEIGHT*landmarks[0].y] , "Left-Shoulder" : [WIDTH *landmarks[11].x,HEIGHT*landmarks[11].y] , "Right-Shoulder" : [WIDTH *landmarks[12].x,HEIGHT*landmarks[12].y] , "Left-Elbow" : [WIDTH *landmarks[13].x,HEIGHT*landmarks[13].y] , "Right-Elbow" : [WIDTH *landmarks[14].x,HEIGHT*landmarks[14].y] , "Left-Wrist" : [WIDTH *landmarks[15].x,HEIGHT*landmarks[15].y] , "Right-Wrist" : [WIDTH *landmarks[16].x,HEIGHT*landmarks[16].y], "Left-Hip" : [WIDTH *landmarks[23].x,HEIGHT*landmarks[23].y], "Right-Hip" : [WIDTH *landmarks[24].x,HEIGHT*landmarks[24].y], "Left-Knee" : [WIDTH *landmarks[25].x,HEIGHT*landmarks[25].y], "Right-Knee" : [WIDTH *landmarks[26].x,HEIGHT*landmarks[26].y], "Left-Ankle" : [WIDTH *landmarks[27].x,HEIGHT*landmarks[27].y], "Right-Ankle" : [WIDTH *landmarks[28].x,HEIGHT*landmarks[28].y] , "Left-Sword" : [0,0] , "Right-Sword" : [0,0]}
                f.write(str(coordinates)+"\n")
            except :
                pass

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)

            cv2.imshow("Mediapipe Feed" , image)

            if cv2.waitKey(10) & 0xFF == ord('q') :
                break


    capture.release()
    cv2.destroyAllWindows()
    f.close()