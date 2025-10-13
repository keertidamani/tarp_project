import torch
from ultralytics import YOLO
model = YOLO("best.pt") 

def detect_defect(image_path):
    results = model(image_path)

    severity_counts = {
        'corrosion_low': 0,
        'corrosion_moderate': 0,
        'corrosion_severe': 0
    }

    for result in results:
        names = result.names
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls.item())
            label = names[class_id]
            confidence = float(box.conf.item())
            print(f"Detected: {label} with Confidence: {confidence * 100:.2f}%")

            if label == "Corrosion_low":
                severity_counts['corrosion_low'] += 1
            elif label == "Corrosion_moderate":
                severity_counts['corrosion_moderate'] += 1
            elif label == "Corrosion_severe":
                severity_counts['corrosion_severe'] += 1

    print("\nDetected severity counts:", severity_counts)
    if severity_counts['corrosion_severe'] > 0:
        lifetime_years = 2
    elif severity_counts['corrosion_moderate'] > 0:
        lifetime_years = 5
    elif severity_counts['corrosion_low'] > 0:
        lifetime_years = 10
    else:
        lifetime_years = 15

    print(f"\nPredicted Lifetime Estimate: {lifetime_years} years")

    if lifetime_years < 15:
        print("Defects detected! Consider maintenance or replacement.")
    else:
        print("No defects detected. Machine is healthy.")

# Example usage
detect_defect("corrosion.jpg")



