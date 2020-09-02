from gpiozero import AngularServo
import RPi.GPIO as GPIO    
from time import sleep
import sys

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

def forward():
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.cleanup()

def left():
    servo.angle = -20  //left
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.cleanup()


def right():
    servo.angle = 35  //right
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.cleanup()

def stop():
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.cleanup()

def backward():
    servo.angle = 5  //straight
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.cleanup()