import RPi.GPIO as GPIO    
from time import sleep

in1 = 24
in2 = 23
enA = 25

in3 = 5
in4 = 6
enB = 13

GPIO.setmode(GPIO.BCM)

#Motor A
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

p1=GPIO.PWM(enA,1000)
p1.start(25)

#Motor B
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p2=GPIO.PWM(enB,1000)
p2.start(25)

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def low():
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)  
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def medium():
    p1.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def high():
    p1.ChangeDutyCycle(75)
    p2.ChangeDutyCycle(75)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
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


