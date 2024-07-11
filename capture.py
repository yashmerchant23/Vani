
import cv2
import time
import os

folder = "frames"

current_directory = os.getcwd()
frames_dir = os.path.join(current_directory, folder)       # creates a path for the new folder in the directory
os.makedirs(frames_dir, exist_ok=True)  # create a folder in the same directory if it already does not exist
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

# Track the timestamp of the last saved image
last_saved_time = time.time()  # to save first image after exactly 10 sec


# Capture frames
while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame")
        break

    # Display frame in "Live Feed" window (no delay)
    cv2.imshow("Live Feed", frame)

    # Check if it's time to save a new image (every 10 seconds)
    if time.time() - last_saved_time >= 10:
        # Save the frame
        cv2.imwrite(path, frame)
        last_saved_time = time.time()  # Update last saved time

        # Print the message only once after saving a new image
        print("You are being watched 👀")

        # Display frame in "Delayed Feed" window
        cv2.imshow("Delayed Feed", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()

