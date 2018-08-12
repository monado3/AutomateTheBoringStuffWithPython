import pyautogui
print('press Ctrl-C to suspend')

try:
    while True:
        x, y = pyautogui.position()
        position_str = f'\rX: {str(x).rjust(4)} Y:{str(y).rjust(4)}'
        print(position_str, end='',flush=True)
except KeyboardInterrupt:
    print('finish')