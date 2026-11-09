import pyautogui

def play_pause():
    pyautogui.press("space")

def next_track():
    pyautogui.hotkey("ctrl", "right")

def previous_track():
    pyautogui.hotkey("ctrl", "left")

def volume_up():
    pyautogui.hotkey("ctrl", "up")

def volume_down():
    pyautogui.hotkey("ctrl", "down")

def like_unlike():
    pyautogui.hotkey("alt", "shift", "b")
