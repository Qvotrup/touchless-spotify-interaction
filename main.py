import cv2
import mediapipe as mp
import time

import gestures
import spotify_controls


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

last_action_time = 0
action_delay = 1.0
last_action_text = "No action"

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    current_time = time.time()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            if current_time - last_action_time > action_delay:
                if gestures.is_thumb_touching_index(hand_landmarks):
                    spotify_controls.next_track()
                    last_action_text = "Next track"
                    last_action_time = current_time

                elif gestures.is_thumb_touching_middle(hand_landmarks):
                    spotify_controls.previous_track()
                    last_action_text = "Previous track"
                    last_action_time = current_time

                elif gestures.is_thumb_touching_ring(hand_landmarks):
                    spotify_controls.volume_up()
                    last_action_text = "Volume up"
                    last_action_time = current_time

                elif gestures.is_thumb_touching_pinky(hand_landmarks):
                    spotify_controls.volume_down()
                    last_action_text = "Volume down"
                    last_action_time = current_time

                elif gestures.is_l_shape(hand_landmarks):
                    spotify_controls.like_unlike()
                    last_action_text = "Like/unlike"
                    last_action_time = current_time

                elif gestures.is_closed_fist(hand_landmarks):
                    spotify_controls.play_pause()
                    last_action_text = "Play/Pause"
                    last_action_time = current_time


    cv2.putText(
        frame,
        "Action: " + last_action_text,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Touchless Spotify Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()