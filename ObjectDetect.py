import cv2
import time
import ollama

folder = "frames"

# initializing the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not started......")
    exit()


# Capture frames
while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame")
        break

    # Display the frame
    cv2.imshow("Camera", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera
cap.release()




