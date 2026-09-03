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

▶️ Usage
Place your input video as input_video.mp4 in the project folder.

Run the script:

bash
python intrusion_detection.py
The processed video will be saved as output_video.mp4.

📂 Project Structure
Code
├── intrusion_detection.py   # Main script
├── input_video.mp4          # Input video
├── output_video.mp4         # Output video (generated)
🎯 Demo
Restricted zone is drawn in blue/green.

Turns red with warning text when a person enters.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

Code

---

## 💼 LinkedIn Post

Here’s a professional yet engaging LinkedIn post you can use:

---

🚨 **Building Smarter Security with AI** 🚨  

I just completed a hands‑on project: an **Intrusion Detection System** using **Python, OpenCV, and Ultralytics YOLOv8**.  

🔹 It processes video frame‑by‑frame  
🔹 Detects people entering a restricted zone  
🔹 Raises a real‑time warning when intrusion occurs  

This project is designed to be **beginner‑friendly**, with clear comments explaining every step — perfect for anyone starting out in computer vision.  

👉 Check out the GitHub repo for the full code and demo: [Insert your GitHub link here]  

AI isn’t just about theory — it’s about solving real‑world problems. Excited to keep exploring how computer vision can make environments safer and smarter!  

#AI #ComputerVision #YOLOv8 #OpenCV #Python #SecurityTech #Innovation  

---

Would you like me to also draft a **Twitter/X post** version (short and punchy) so you can share it across multiple platforms?
