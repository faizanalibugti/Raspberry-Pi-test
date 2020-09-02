from gpiozero import AngularServo
import RPi.GPIO as GPIO    
from time import sleep
import sys
import tkinter as tk

in1 = 24
in2 = 23
enA = 25

in3 = 5
in4 = 6
enB = 13

GPIO.setmode(GPIO.BCM)

// Motor A
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p1=GPIO.PWM(enA,1000)
p1.start(25)

// Motor B
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p2=GPIO.PWM(enB,1000)
p2.start(25)

servo = AngularServo(17, min_angle=-90, max_angle=90)

def forward(tf):
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(tf)
    GPIO.cleanup()

def left(tf):
    servo.angle = -20  //left
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(tf)
    GPIO.cleanup()


def right(tf):
    servo.angle = 35  //right
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(tf)
    GPIO.cleanup()

def stop(tf):
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(tf)
    GPIO.cleanup()

def backward(tf):
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(tf)
    GPIO.cleanup()

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