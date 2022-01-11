from PyTrackX.module import *

#! YOLO OBJECT TRACKING
yolo_path = "./yolo-coco"
video_path = "input.mp4"
object = "person"
track_object(yolo_path,video_path,object)

#! MEDIAPIPE POSTURE TRACKING
track_posture()