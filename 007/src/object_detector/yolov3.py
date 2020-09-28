# Azhar Mithani
import os
import time
import itertools
import cv2
import numpy as np

# A class defining all the functions used in the detection of People aka PeopleDetector function
class PeopleDetector:
    def __init__(self, yolocfg='yolo_weights/yolov3.cfg',
                 yoloweights='yolo_weights/yolov3.weights',
                 labelpath='yolo_weights/coco.names',
                 confidence=0.5,
                 nmsthreshold=0.4):
        self._yolocfg = yolocfg
        self._yoloweights = yoloweights
        self._confidence = confidence
        self._nmsthreshold = nmsthreshold
        self._labels = open(labelpath).read().strip().split("\n")
        self._colors = np.random.randint(
            0, 255, size=(len(self._labels), 3), dtype="uint8")
        self._net = None
        self._layer_names = None
        self._boxes = []
        self._confidences = []
        self._classIDs = []
        self._centers = []
        self._layerouts = []
        self._MIN_DIST = 150
        self._mindistances = {}
        
# Loading the yolov3 network backend

    def load_network(self):
        self._net = cv2.dnn.readNetFromDarknet(
            self._yolocfg, self._yoloweights)
        self._net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self._net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        self._layer_names = [self._net.getLayerNames()[i[0] - 1]
                             for i in self._net.getUnconnectedOutLayers()]
        print("yolov3 loaded successfully\n")

# Function calculating time for prediction
    def predict(self, image):
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                     [0, 0, 0], 1, crop=False)
        self._net.setInput(blob)
        start = time.time()
        self._layerouts = self._net.forward(self._layer_names)
        end = time.time()
        print("yolo took {:.6f} seconds".format(end - start))
        return(self._layerouts)
    
# Function performing prediction

    def process_preds(self, image, outs):
        (frameHeight, frameWidth) = image.shape[:2]
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                if classId != 0:  # filter person class
                    continue
                confidence = scores[classId]
                if confidence > self._confidence:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    self._classIDs.append(classId)
                    self._confidences.append(float(confidence))
                    self._boxes.append([left, top, width, height])
                    self._centers.append((center_x, center_y))
        indices = cv2.dnn.NMSBoxes(
            self._boxes, self._confidences, self._confidence, self._nmsthreshold)
        for i in indices:
            i = i[0]
            box = self._boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            self.draw_pred(image, self._classIDs[i], self._confidences[i], left,
                           top, left + width, top + height)
        return self._centers
    
# Function initializing variables

    def clear_preds(self):
        self._boxes = []
        self._confidences = []
        self._classIDs = []
        self._centers = []
        self._layerouts = []
        self._mindistances = {}

# Function drawing prediction based on frames
        
    def draw_pred(self, frame, classId, conf, left, top, right, bottom):
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
        label = '%.2f' % conf
        label = '%s:%s' % (self._labels[classId], label)
        labelSize, baseLine = cv2.getTextSize(
            label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        top = max(top, labelSize[1])
        cv2.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(
            1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
        cv2.putText(frame, label, (left, top),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)

        self.find_min_distance(self._centers)
        for k in self._mindistances:
            cv2.line(frame, k[0], k[1], (0, 0, 255), 7)
            
# Function returning minimum euclidean distance between predicted anchor boxes

    def find_min_distance(self, centers):
        '''
        return min euclidean distance between predicted anchor boxes
        '''
        centers = self._centers
        comp = list(itertools.combinations(centers, 2))
        for pts in comp:
            ecdist = np.linalg.norm(np.asarray(pts[0])-np.asarray(pts[1]))
            if ecdist < self._MIN_DIST:
                self._mindistances.update({pts: ecdist})
