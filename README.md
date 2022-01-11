<h1 align="center">PyTrackX</h1>
A general python framework for visual object tracking.
PyTrackX is a  Python package that serves as an automated tool which tracks different objects and body movements as per user requirement and returns the real-time coordinates with very less steps and a simple video input.

## Functions
### **track_object(yolo_path,video_path,object,min_conf)**
```
* yolo_path: folder path for the download yolo model files (STRING)
* video_path: file path of video input feed
* object: any object name from list of objects YOLO can detect. 
* min_conf (default parameter): confidence level for an object detected (default value is 0.5)
```

Returns a text file with coordinates of each object detected per frame as tracked frame to frame.

### **track_posture(width,height,video_path,min_dconf,min_tconf)**
```
* width (default parameter): frame width
* height (default parameter): frame height
* video_path (default parameter): file path of video input feed (default value (0)- Live webcam video feed as input)
* min_dconf: confidence level for an object detected
* min_tconf: confidence level for an object tracking
```

Returns a text file with corrdinates of all landmarks detected by <a href="https://mediapipe.dev/"> Mediapipe </a> per frame as tracked frame to frame with respect to the frame width and height.<br>
<img src="https://user-images.githubusercontent.com/68152189/148942731-301e8b0e-99d0-40b2-9e44-1f1ca33d5a95.png" width="500" height="400" />                                                                                                                                      

## User Installation
### Install Package
```
pip install PyTrackX
```
Download yolo-coco folder from <a href="https://drive.google.com/drive/folders/1PGgWb-8yNSJNiHQF_Av6EHqBSEdiRhFp?usp=sharing">here</a> into your **current working directory**. Rename the folder **yolo-coco** if otherwise. The folder contains the following files:
```
* coco.name
* yolo3.cfg
* yolo3.weights
```

Another option  is to download via git:
### Git Install

```
    pip install git+https://github.com/swetha4444/PyTrackX.git
```

You can also clone the repository:
### Clone Repository
```
    git clone https://github.com/swetha4444/PyTrackX.git
    pip install -r requirements.txt
    python setup.py install
```

### Dependencies:
```
* 'numpy>=1.11'
* 'matplotlib>=1.5'
* 'pandas'
* cv2'
* 'scipy'
* 'mediapipe'
* 'time'
```

## Usage
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
