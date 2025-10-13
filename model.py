from ultralytics import YOLO
data_path = 'D:/Keerti2024/VIT Sem7/tarp/defects final.v3i.yolov8/data.yaml'  
model = YOLO("best.pt")
model.train(data=data_path, epochs=100, imgsz=640, batch=8, workers=2, device=0)
