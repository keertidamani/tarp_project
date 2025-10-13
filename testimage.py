from ultralytics import YOLO
import cv2
model = YOLO('best.pt')
img = cv2.imread('corrosion.jpg') 
results = model(img)
result = results[0]
result.show() 
