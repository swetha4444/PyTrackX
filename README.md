# PyTrackX
A general python framework for visual object tracking.
PyTrackX is a work in progress Python package that serves as an automated tool which tracks different objects and body movements as per user requirement and returns the real-time coordinates with very less steps and a simple video input.

## Usage
### Install package
```
pip install PyTrackX
```
### YOLO OBJECT TRACKING
```
from PyTrackX import *
yolo_path = "./yolo-coco"
video_path = "input.mp4"
object = "person"
track_object(yolo_path,video_path,object)
```

### MEDIAPIPE POSTURE TRACKING
track_posture()