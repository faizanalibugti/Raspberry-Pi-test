import RPi.GPIO as GPIO    
from time import sleep

in1 = 18
in2 = 16
enA = 22

GPIO.setmode(GPIO.BOARD)

// Motor A
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p1=GPIO.PWM(enA,1000)
p1.start(25)

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.cleanup()

def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.cleanup()

def low():
    p1.ChangeDutyCycle(25)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.cleanup()

def medium():
    p1.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.cleanup()

def high():
    p1.ChangeDutyCycle(75)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.cleanup()

forward()
sleep(10)

backward()
sleep(10)

low()
sleep(10)

medium()
sleep(10)

high()
sleep(10)