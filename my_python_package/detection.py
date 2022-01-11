# import the necessary packages
from .config import NMS_THRESH, MIN_CONF, People_Counter
import numpy as np
import cv2

def detect_boundary(frame, net, ln, confidence_value ,personIdx=0):
	(H, W) = frame.shape[:2]
	results = []

	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	layerOutputs = net.forward(ln) #numpy op of layers

	boxes = []
	centroids = []
	confidences = []
	dets = []

	for output in layerOutputs:
		for detection in output:
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			if classID == personIdx and confidence > confidence_value:
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				boxes.append([x, y, int(width), int(height)])
				centroids.append((centerX, centerY))
				confidences.append(float(confidence))
				dets.append([x, y, int(width), int(height),float(confidence)])
    
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, MIN_CONF, NMS_THRESH) #Non-max supression

	if People_Counter:
		human_count = "People Count: {}".format(len(idxs))
		cv2.putText(frame, human_count, (frame.shape[0] - 170, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),2)

	if len(idxs) > 0:
		for i in idxs.flatten(): 
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])

			r = (confidences[i], (x, y, x + w, y + h), centroids[i])
			results.append(r)

	return results,boxes,idxs,dets,centroids
