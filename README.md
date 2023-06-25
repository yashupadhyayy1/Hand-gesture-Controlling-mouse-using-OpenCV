# Hand Gesture Mouse Controlling

This project enables controlling the computer mouse using hand gestures captured by a webcam. It utilizes the OpenCV and Mediapipe libraries to detect and track hand landmarks, and performs actions based on specific gestures.

## Prerequisites

- Python 3.x
- OpenCV library
- Mediapipe library
- Numpy library
- PyAutoGUI library

## Project Structure

The project consists of two main files:

1. `handtracking2d.py`: This file contains the `handDetector` class, which encapsulates the hand detection and tracking functionality. It utilizes the `mpHands` module from Mediapipe to detect hand landmarks and provides methods for finding hands, positions, finger states, distances, etc. The `main` function sets up the webcam, initializes the `handDetector`, and continuously processes video frames to detect and track hand gestures.

2. `mouse.py`: This file enables mouse control using hand gestures. It imports the `handDetector` class from `handtracking2d.py` and utilizes it to detect hand landmarks and recognize specific gestures. It captures video frames from the webcam, tracks the movement of the index finger, and moves the mouse cursor accordingly. It also detects when the index and middle fingers are close together to simulate a mouse click.

## Usage

1. Install the necessary libraries by running the following command:

   ```shell
   pip install opencv-python mediapipe numpy pyautogui

##Notes
The project assumes that a single hand is being tracked at a time. If multiple hands are present, only the first detected hand will be considered for mouse control.
The project incorporates smoothening techniques to reduce cursor jitter and improve usability.
The project provides visual feedback by overlaying circles on the video frames to indicate the active modes (moving or clicking) and the cursor position.
