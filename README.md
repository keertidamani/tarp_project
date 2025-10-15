
---

## 🧾 SMART MACHINE DEFECT PROTECTION SYSTEM
📦 **GitHub Repository:**  
👉 [https://github.com/keertidamani/tarp_project](https://github.com/keertidamani/tarp_project)

This repository contains:
- Full source code (`model.py`, `testimage.py`, `videodetection.py`, `webcam.py`, `lifetime.py`)  
- Trained YOLOv8 model weights (`best.pt`)  
- Sample datasets and images (`welding6.jpg`, `corrosion.jpg`, `video.mp4`)  
- Supporting documentation and example media  

---

## 🧠 Tools and Technologies
- **Deep Learning Framework:** Ultralytics YOLOv8  
- **Programming Language:** Python 3.10+  
- **Libraries:** OpenCV, NumPy, Pandas, Matplotlib, Seaborn  
- **Training Platform:** Google Colab Pro+ (NVIDIA T4 GPU)  
- **Dataset Annotation & Augmentation:** Roboflow  

---

## ⚙️ Installation and Setup

### 🧰 Complete Setup Instructions

```bash
1️⃣ Clone the Repository
git clone https://github.com/keertidamani/tarp_project.git
cd tarp_project

2️⃣ Install Dependencies
pip install ultralytics opencv-python numpy pandas matplotlib seaborn

3️⃣ Run the System

🖼️ For Image Detection
python testimage.py

🎥 For Video Detection
python videodetection.py

📷 For Live Webcam Detection
python webcam.py

💡 Tip:
# Press 'Q' on your keyboard to close the OpenCV window after viewing detections.
# The system will automatically draw bounding boxes, class labels, and confidence scores.
```
## 📊 Performance Summary
| Metric | Result |
|--------|---------|
| **mAP@0.5** | 49.4% |
| **mAP@0.5:0.95** | 34.5% |
| **Precision** | 50.1% |
| **Recall** | 52.6% |
| **FPS (GPU)** | 25 |
| **FPS (CPU)** | 7 |

## 🧑‍💻 Authors
- **Santhi K.** – *Project Supervisor, SCOPE, VIT Vellore*  
- **Keerti Damani** – *22BBS0174*  
- **Yash Agarwal** – *22BBS0161*  











