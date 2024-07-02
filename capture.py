import cv2
import time
import os

folder = "frames"

current_directory = os.getcwd()
frames_dir = os.path.join(current_directory, folder)       # creates a path for the new folder in the directory
os.makedirs(frames_dir, exist_ok=True)  #create a folder in the same directory if it already does not exists
path = f"{folder}/frame.jpg"

# initializing the webcam
cap = cv2.VideoCapture(0)

# Create a resizable window
cv2.namedWindow("Live Feed", cv2.WINDOW_NORMAL)
cv2.namedWindow("Delayed Feed", cv2.WINDOW_NORMAL)

# Check if the webcam is opened correctly
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

    # Display frame in "Live Feed" window (no delay)
    cv2.imshow("Live Feed", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

    # Display frame in "Delayed Feed" window with a 2-second delay
    if time.time() % 2 < 1:           # we dont stop the time we only save/show the frame when time is multiple of 2
        cv2.imshow("Delayed Feed", frame)
        # Save the frame
        cv2.imwrite(path, frame)  # saving the latest frame in the folder by replacing the previous one(as they both are named the same)
        print("You are being watched 👀")

# Release the camera
cap.release()
cv2.destroyAllWindows()

