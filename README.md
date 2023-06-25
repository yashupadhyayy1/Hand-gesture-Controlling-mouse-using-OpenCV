# Hand Gesture Mouse Controlling

This project utilizes hand tracking and computer vision techniques to control the mouse cursor using hand gestures. By detecting and tracking hand landmarks, it enables the user to move the mouse cursor and perform click actions using specific hand gestures.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- OpenCV (cv2)
- Mediapipe
- Numpy
- PyAutoGUI

You can install the required libraries using pip:

```sudo
pip install opencv-python mediapipe numpy pyautogui
```


## Usage

1. Run the `handtracking2d.py` script to enable hand tracking and landmark detection.

   ```bash
   python handtracking2d.py

This script uses the computer's webcam to capture video frames and detects hand landmarks using the Mediapipe library. The hand landmarks are displayed on the video feed.

Once the hand landmarks are detected, you can control the mouse cursor using the following gestures:

Moving Mode: Extend your index finger while keeping other fingers closed. Move your hand to control the mouse cursor. The cursor position will follow the movement of your index finger.

Clicking Mode: Extend both your index and middle fingers. Bring the tips of the fingers close together to trigger a mouse click. The cursor will display a circle when the fingers are close enough, indicating that a click action will be performed.

The mouse.py script should be run alongside the `handtracking2d.py` script.
This script uses the hand landmarks detected by handtracking2d.py to control the mouse cursor on the screen. The cursor position is mapped to the detected hand movement, and click actions are performed based on the hand gesture.

The video feed from the webcam will display the hand landmarks and the movement of the mouse cursor. The script also shows the frame rate (FPS) on the screen.

Press the Esc key to exit the program.

Note: Adjustments to the frame size and other parameters can be made in the code to fit your specific webcam setup and hand movement preferences.

Conclusion
The hand gesture mouse controlling project enables users to control the mouse cursor using specific hand gestures. By leveraging hand tracking and computer vision techniques, it provides a hands-free and intuitive way to interact with the computer, opening up possibilities for various applications and accessibility improvements.
