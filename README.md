# PyTrackX
A general python framework for visual object tracking.
PyTrackX is a work in progress Python package that serves as an automated tool which tracks different objects and body movements as per user requirement and returns the real-time coordinates with very less steps and a simple video input.

## Functions
### **track_object(yolo_path,video_path,object,min_conf)**
* yolo_path: folder path for the download yolo model files (STRING)
* video_path: file path of video input feed
* object: any object name from list of objects YOLO can detect. 
* min_conf (default parameter): confidence level for an object detected (default value is 0.5)

### **track_posture(width,height,video_path,min_dconf,min_tconf)**
* width
* height
* video_path
* min_dconf
* min_tconf

## Usage
### Install package
```
pip install PyTrackX
```
### YOLO Object Tracking
```
from PyTrackX import *
yolo_path = "./yolo-coco"
video_path = "input.mp4"
object = "person"
track_object(yolo_path,video_path,object)
```

### Mediapipe Posture Tracking
```
from PyTrackX import *
track_posture()
```
