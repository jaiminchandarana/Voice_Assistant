from pynput.mouse import Listener

# This function will be called every time the mouse moves
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# Setting up the listener to track mouse movements
with Listener(on_move=on_move) as listener:
    listener.join()
