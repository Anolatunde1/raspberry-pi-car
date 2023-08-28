# //import RPi.GPIO as gpio
import time

from pynput import keyboard


# gpio.setmode(gpio.BOARD)

# gpio.setup(3, gpio.OUT) #Setting Pinmode
# gpio.setup(5, gpio.OUT) #Setting Pinmode
# gpio.setup(7, gpio.OUT) #Setting Pinmode
# gpio.setup(11, gpio.OUT)#Setting Pinmode
# gpio.setwarnings(False)
def forward():
    print('1')


def backward():
    print('2')


def left():
    print('3')


def right():
    print('4')


def on_press(key):

    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['w', 's', 'a', 'd']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        #print('Key pressed: ' + k)
        # return False  # stop listener; remove this if want more keys

        if(k == 'w'):
            forward()
        if(k == 's'):
            backward()
        if(k == 'a'):
            left()
        if(k == 'd'):
            right()



listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on wa separate thread
listener.join()  # remove if main thread is polling self.keys

# Functions
