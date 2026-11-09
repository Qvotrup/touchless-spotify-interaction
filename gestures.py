import math


def distance(point1, point2):
    return math.sqrt(
        (point1.x - point2.x) ** 2 +
        (point1.y - point2.y) ** 2
    )


def is_thumb_touching_index(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]

    return distance(thumb_tip, index_tip) < 0.04


def is_thumb_touching_middle(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    middle_tip = hand_landmarks.landmark[12]

    return distance(thumb_tip, middle_tip) < 0.04

def is_thumb_touching_ring(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    ring_tip = hand_landmarks.landmark[16]

    return distance(thumb_tip, ring_tip) < 0.04

def is_thumb_touching_pinky(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    pinky_tip = hand_landmarks.landmark[20]

    return distance(thumb_tip, pinky_tip) < 0.04


def is_finger_up(hand_landmarks, tip_id, pip_id):
    tip = hand_landmarks.landmark[tip_id]
    pip = hand_landmarks.landmark[pip_id]

    return tip.y < pip.y

def is_thumb_up(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]

    return thumb_tip.x > thumb_ip.x



def is_closed_fist(hand_landmarks):
    index_up = is_finger_up(hand_landmarks, 8, 6)
    middle_up = is_finger_up(hand_landmarks, 12, 10)
    ring_up = is_finger_up(hand_landmarks, 16, 14)
    pinky_up = is_finger_up(hand_landmarks, 20, 18)


    return (
            not index_up and
            not middle_up and
            not ring_up and
            not pinky_up
            )

def is_l_shape(hand_landmarks):
    thumb_up = is_thumb_up(hand_landmarks)
    index_up = is_finger_up(hand_landmarks, 8, 6)
    middle_up = is_finger_up(hand_landmarks, 12, 10)
    ring_up = is_finger_up(hand_landmarks, 16, 14)
    pinky_up = is_finger_up(hand_landmarks, 20, 18)

    return(
        thumb_up and
        index_up and
        not middle_up and
        not ring_up and
        not pinky_up
    )