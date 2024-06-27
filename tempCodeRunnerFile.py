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
cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)

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

    # Display the frame
    cv2.imshow("Camera", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

    print("Smile!😁📸")
    cv2.imwrite(path, frame)  # saving the latest image in the folder by replacing the existing one

    # the 2 second diff
    time.sleep(2)

# Release the camera
cap.release()
cv2.destroyAllWindows()
