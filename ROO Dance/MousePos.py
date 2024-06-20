import tkinter
import time

print('Press Ctrl-C to quit.')
p=tkinter.Tk()

try:
    while True:
        x, y = p.winfo_pointerxy()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(1)
        
except KeyboardInterrupt:
    print('\n') 