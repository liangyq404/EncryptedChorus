
import RPi.GPIO as GPIO
import time

# set up gpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)    # PWMA
GPIO.setup(13, GPIO.OUT)    # AIN2    
GPIO.setup(16, GPIO.OUT)    # AIN1
GPIO.setup(20, GPIO.OUT)    # STBY

# enable board
GPIO.output(20, GPIO.HIGH)

# set PWMA high for testing can be set to a PWM output for motor speed control
#GPIO.output(12, GPIO.HIGH)
p = GPIO.PWM(12,100)
p.start(0)

# Run motor in direction A for 5 seconds
p.ChangeDutyCycle(25)
GPIO.output(13, GPIO.HIGH)
GPIO.output(16, GPIO.LOW)
time.sleep(5)


# stop motor for 5 seconds
GPIO.output(13, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
time.sleep(5)

# Run motor in direction B for 5 seconds
GPIO.output(13, GPIO.LOW)
GPIO.output(16, GPIO.HIGH)
time.sleep(5)

# stop motor for 5 seconds
GPIO.output(13, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
time.sleep(5)
