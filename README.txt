Touchless interaction controls for Spotify

Description
This project allows a user to interact with the Spotify Desktop application by using hand gestures captured with a webcam.
The program detects the relevant gestures using MediaPipe Hands, and triggers keyboard inputs corresponding to Spotify Desktop's built-in keyboard shortcuts

Requirements
- Windows
- Python 3.12
- Webcam
- Spotify Desktop application for Windows
- The used python libraries are listed in requirements.txt

Running the program
1. Open Spotify Desktop
2. Run main.py
3. Make sure Spotify Desktop is the active window
4. Perform the supported hand gestures
Exit: to exit the program, press the Q key


Supported gestures
- touch index finger to thumb: skip (next song)
- touch middle finger to thumb: go back (previous song)
- touch ring finger to thumb: volume up
- touch pinky finger to thumb: volume down
- thumb and index finger out with closed fist(L sign): like/unlike song
- closed fist: play/pause song
- it is recommended to keep an open palm with spread fingers as a neutral/resting position