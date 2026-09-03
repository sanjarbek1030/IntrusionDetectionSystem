# Intrusion Detection System with YOLOv8 and OpenCV

This project demonstrates a beginner‑friendly **Intrusion Detection System** built with **Python, OpenCV, and Ultralytics YOLOv8**.  
It detects people entering a restricted zone in a video and raises a warning.

---

## 🚀 Features
- Loads an input video (`input_video.mp4`) and saves processed output (`output_video.mp4`).
- Defines a custom restricted zone polygon (adjustable coordinates).
- Draws the zone with a semi‑transparent overlay.
- Runs YOLOv8 object detection, filtering only for the **person** class.
- Checks if a person’s feet position enters the restricted zone.
- Displays **WARNING: INTRUSION DETECTED** when intrusion occurs.
- Saves every processed frame into the output video.

---

## 🛠️ Requirements
- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

Install dependencies:
```bash
pip install opencv-python ultralytics
