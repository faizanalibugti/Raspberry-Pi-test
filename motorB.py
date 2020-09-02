import RPi.GPIO as GPIO    
from time import sleep

in3 = 5
in4 = 6
enB = 13

GPIO.setmode(GPIO.BCM)

#Motor B
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p2=GPIO.PWM(enB,1000)
p2.start(25)

def forward():
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def backward():
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def low():
    p2.ChangeDutyCycle(25)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def medium():
    p2.ChangeDutyCycle(50)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def high():
    p2.ChangeDutyCycle(75)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

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
