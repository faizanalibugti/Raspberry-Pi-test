from time import sleep
import sys
import tkinter as tk

def forward(tf):
    print('forward')
    sleep(tf)
    
def left(tf):
    print('left')
    sleep(tf)
    

def right(tf):
    print('right')
    sleep(tf)
   
def stop(tf):
    print('stop')
    sleep(tf)
    
def backward(tf):
    print('backward')
    time.sleep(tf)
    
def key_input(event):
    print('Key: ', event.char)
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        stop(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()   