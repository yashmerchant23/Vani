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

# Initialize flag to track new image saved and message printed
new_image_saved = False
message_printed = False

# Capture frames
while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame")
        break

    # Display frame in "Live Feed" window (no delay)
    cv2.imshow("Live Feed", frame)

    # Display frame in "Delayed Feed" window with a 2-second delay
    if time.time() % 3 < 1:  # Display only during certain intervals
        cv2.imshow("Delayed Feed", frame)
        # Save the frame if it's time to do so
        cv2.imwrite(path, frame)  # Saving the latest frame in the folder by replacing the previous one (since they are named the same)

        # Check if a new image is saved
        if not new_image_saved:
            new_image_saved = True
            message_printed = False  # Reset message_printed flag

        # Print the message only once after a new image is saved
        if new_image_saved and not message_printed:
            print("You are being watched 👀")
            message_printed = True  # Set flag to indicate message has been printed

    else:
        new_image_saved = False  # Reset new_image_saved flag if no image saved this time

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()


