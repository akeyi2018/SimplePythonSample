from pynput import keyboard
from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)

kb = Listener(on_press=on_press)

kb.start()

print("OK")

kb.stop()
