import RPi.GPIO as GPIO
 
# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)
 
# set up the GPIO channels - one input and one output
#GPIO.setup(7, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
 
# input from GPIO7
input_value = GPIO.input(24)
 
# output to GPIO8
if input_value > 0:
    print("Spengo")
    GPIO.output(24, False)
else:
    print("Accendo")
    GPIO.output(24, True)


# clean up
GPIO.cleanup()

