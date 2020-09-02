from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=-90, max_angle=90)

while True:
    servo.angle = -20 //left
    sleep(4)
    servo.angle = 5 //straight
    sleep(4)
    servo.angle = 35 //right
    sleep(4)