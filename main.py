# Import necessary libraries
import cv2  # OpenCV for video processing and drawing
from ultralytics import YOLO  # Ultralytics YOLOv8 for object detection
import numpy as np

# -----------------------------
# Step 1: Load the input video
# -----------------------------
video_path = "input_video.mp4"  # Name of the input video file
cap = cv2.VideoCapture(video_path)  # Open the video file for reading

# Get video properties (width, height, frames per second)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # Width of the video
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Height of the video
fps = cap.get(cv2.CAP_PROP_FPS)                        # Frames per second

# -----------------------------
# Step 2: Set up video writer
# -----------------------------
# Define the codec (video compression format)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# Create a VideoWriter object to save processed frames
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (frame_width, frame_height))

# -----------------------------
# Step 3: Define restricted zone
# -----------------------------
# Example polygon coordinates for a 1280x720 video
# You can adjust these points to change the restricted area
restricted_zone = [(400, 400), (880, 400), (880, 700), (400, 700)]

# -----------------------------
# Step 4: Load YOLOv8 model
# -----------------------------
# Load the pretrained YOLOv8n model (nano version, fast and small)
model = YOLO("yolov8n.pt")

# -----------------------------
# Step 5: Process video frames
# -----------------------------
while cap.isOpened():  # Loop until video ends
    ret, frame = cap.read()  # Read one frame
    if not ret:  # If no frame is returned, break the loop
        break

    # -----------------------------
    # Draw restricted zone overlay
    # -----------------------------
    # Create a copy of the frame to draw semi-transparent overlay
    overlay = frame.copy()
    # Draw filled polygon with blue color (BGR: 255,0,0)
    cv2.fillPoly(overlay, [np.array(restricted_zone, dtype=np.int32)], (255, 0, 0))
    # Blend overlay with original frame (alpha=0.3 for transparency)
    frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

    # Draw polygon outline (green by default)
    zone_color = (0, 255, 0)  # Green
    cv2.polylines(frame, [np.array(restricted_zone, dtype=np.int32)], True, zone_color, 2)

    # -----------------------------
    # Run YOLOv8 detection
    # -----------------------------
    results = model(frame)  # Run detection on the frame

    intrusion_detected = False  # Flag to check if intrusion happens

    # Loop through detected objects
    for result in results:
        for box in result.boxes:  # Each bounding box
            cls_id = int(box.cls[0])  # Class ID of detected object
            if cls_id == 0:  # Class 0 = "person"
                # Get bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                # Calculate center-bottom point (feet position)
                feet_x = int((x1 + x2) / 2)
                feet_y = int(y2)

                # Draw bounding box around person
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
                # Draw a small circle at feet position
                cv2.circle(frame, (feet_x, feet_y), 5, (0, 0, 255), -1)

                # -----------------------------
                # Step 6: Check intrusion
                # -----------------------------
                # Use pointPolygonTest to check if feet point is inside restricted zone
                inside = cv2.pointPolygonTest(np.array(restricted_zone, dtype=np.int32), (feet_x, feet_y), False)
                if inside >= 0:  # If point is inside polygon
                    intrusion_detected = True

    # If intrusion detected, change zone outline to red and show warning text
    if intrusion_detected:
        zone_color = (0, 0, 255)  # Red
        cv2.polylines(frame, [np.array(restricted_zone, dtype=np.int32)], True, zone_color, 3)
        cv2.putText(frame, "WARNING: INTRUSION DETECTED", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4, cv2.LINE_AA)

    # -----------------------------
    # Step 7: Save processed frame
    # -----------------------------
    out.write(frame)  # Write the frame into output video

# -----------------------------
# Step 8: Release resources
# -----------------------------
cap.release()  # Release video capture
out.release()  # Release video writer
cv2.destroyAllWindows()  # Close all OpenCV windows
