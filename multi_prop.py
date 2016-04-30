import sys
import time
import subprocess as sub

def check_apm():
    ret = sub.call(["ps -AT | grep -c sched-timer > /dev/null"], shell = True)
    if ret <= 0:
        sys.exit("APM is running. Can't launch the example")

class PWM():

    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        #c1
        try:
            with open("/sys/class/pwm/pwmchip0/export", "a") as pwm_export:
                pwm_export.write(str(self.c1))
        except IOError:
            #already exported. nothing to 
            pass
        
        with open("/sys/class/pwm/pwmchip0/pwm%d/enable" % self.c1, "w") as pwm_enable:
            pwm_enable.write("1")

    def set_period(self, freq):
        period_ns = int(1e9/freq)
        with open("/sys/class/pwm/pwmchip0/pwm%d/period" % self.c1, "w") as pwm_period:
            pwm_period.write(str(period_ns))

    def set_duty_cycle(self, period):
        period_ns = int(period*1e6)
        with open("/sys/class/pwm/pwmchip0/pwm%d/duty_cycle" % self.c1, "w") as pwm_duty:
            pwm_duty.write(str(period_ns))
    #c2
     	try:
            with open("/sys/class/pwm/pwmchip0/export", "a") as pwm_export:
                pwm_export.write(str(self.c2))
        except IOError:
            #already exported. nothing to 
            pass
        
        with open("/sys/class/pwm/pwmchip0/pwm%d/enable" % self.c2, "w") as pwm_enable:
            pwm_enable.write("1")

    def set_period(self, freq):
        period_ns = int(1e9/freq)
        with open("/sys/class/pwm/pwmchip0/pwm%d/period" % self.c2, "w") as pwm_period:
            pwm_period.write(str(period_ns))

    def set_duty_cycle(self, period):
        period_ns = int(period*1e6)
        with open("/sys/class/pwm/pwmchip0/pwm%d/duty_cycle" % self.c2, "w") as pwm_duty:
            pwm_duty.write(str(period_ns))
    #c3
     	try:
            with open("/sys/class/pwm/pwmchip0/export", "a") as pwm_export:
                pwm_export.write(str(self.c3))
        except IOError:
            #already exported. nothing to 
            pass
        
        with open("/sys/class/pwm/pwmchip0/pwm%d/enable" % self.c3, "w") as pwm_enable:
            pwm_enable.write("1")

    def set_period(self, freq):
        period_ns = int(1e9/freq)
        with open("/sys/class/pwm/pwmchip0/pwm%d/period" % self.c3, "w") as pwm_period:
            pwm_period.write(str(period_ns))

    def set_duty_cycle(self, period):
        period_ns = int(period*1e6)
        with open("/sys/class/pwm/pwmchip0/pwm%d/duty_cycle" % self.c3, "w") as pwm_duty:
            pwm_duty.write(str(period_ns))
    #c4
     try:
            with open("/sys/class/pwm/pwmchip0/export", "a") as pwm_export:
                pwm_export.write(str(self.c4))
        except IOError:
            #already exported. nothing to 
            pass
        
        with open("/sys/class/pwm/pwmchip0/pwm%d/enable" % self.c4, "w") as pwm_enable:
            pwm_enable.write("1")

    def set_period(self, freq):
        period_ns = int(1e9/freq)
        with open("/sys/class/pwm/pwmchip0/pwm%d/period" % self.c4, "w") as pwm_period:
            pwm_period.write(str(period_ns))

    def set_duty_cycle(self, period):
        period_ns = int(period*1e6)
        with open("/sys/class/pwm/pwmchip0/pwm%d/duty_cycle" % self.c4, "w") as pwm_duty:
            pwm_duty.write(str(period_ns))

#This runs the check_apm function found in util.py.  
#I am not totally sure of code used to detect this, but the function serves to 
#kill the program and alert the user if APM (the flight controller) is running
check_apm()

#This section defines the constants of the example. PWM_OUTPUT is used to initialize the PWM class below, 
#and the min and max set the pulse range for the servo.
PWM_OUTPUT0 = 0
PWM_OUTPUT1 = 1
PWM_OUTPUT2 = 2
PWM_OUTPUT3 = 3
SERVO_MIN = 1.250 #ms
SERVO_MAX = 1.750 #ms

#Here pwm is defined to be a PWM object initialized with PWM_OUTPUT.  
#The set period sets the period of the pulse.
pwm0 = PWM(PWM_OUTPUT0)
pwm1 = PWM(PWM_OUTPUT1)
pwm2 = PWM(PWM_OUTPUT2)
pwm3 = PWM(PWM_OUTPUT3)
pmw0.set_period(50)
pmw1.set_period(50)
pmw2.set_period(50)
pmw3.set_period(50)


while (True):
    pwm0.set_duty_cycle(SERVO_MIN)#runs the servo at minimum
    pwm1.set_duty_cycle(SERVO_MIN)
    pwm2.set_duty_cycle(SERVO_MIN)
    pwm3.set_duty_cycle(SERVO_MIN)