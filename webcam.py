import cv2
from ultralytics import YOLO
model = YOLO("best.pt")  
class_names = model.names 
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print(" Error: Unable to read from webcam")
        break
    results = model(frame, conf=0.25) 
    result = results[0]
    for box in result.boxes:
        cls_id = int(box.cls[0])  # Class index
        conf = float(box.conf[0])  # Confidence
        x1, y1, x2, y2 = map(int, box.xyxy[0]) 
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{class_names[cls_id]}: {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    cv2.imshow("YOLOv8 Live Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


