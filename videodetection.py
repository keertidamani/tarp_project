from ultralytics import YOLO
import cv2
model = YOLO('best.pt')  
cap = cv2.VideoCapture("C:\\Users\\Dell\\Desktop\\tarp\\video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame, imgsz=640, conf=0.25)
    annotated_frame = results[0].plot()
    cv2.imshow('YOLOv8 Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
