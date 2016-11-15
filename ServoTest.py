# To run this file, just do:
# sudo python ServoTest.py

# Just importing Python's standard libraries
import sys
import time
# This is the navio's specific utilities 
import navio.pwm
import navio.util

navio.util.check_apm()

PWM_OUTPUT = 0
# These are just some good values to know when seting the motor power
SERVO_MIN = 1.250 #ms
SERVO_MAX = 1.750 #ms

# Now every time we want to use a motor, we have to enable it first 
# Let's enable all 4 (they're numbered 0-3)
pwmArray = []
for num in range(0,3+1): # This loops over 0,1,2,3
	pwm = navio.pwm.PWM(num)
	pwm.set_period(50)
	pwmArray.append(pwm)

cycles = 3; # How many cycles you want to spin the rotors for 
# Otherwise it'll keep spinning forever

while (cycles > 0):
	cycles -= 1
	# Now we alternate all motors between fast and slow 
	for pwm in pwmArray:
    		pwm.set_duty_cycle(SERVO_MIN)
    	# They will keep spinning until we send a new signal
   	time.sleep(1)
    	for pwm in pwmArray:
    		pwm.set_duty_cycle(SERVO_MAX)
    	time.sleep(1)

# So even if you terminate the script, they will keep spinning
# We have to send a stop signal to every motor before we leave
for pwm in pwmArray:
    pwm.set_duty_cycle(0)
