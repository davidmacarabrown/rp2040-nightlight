from machine import Pin, PWM, ADC
import time

# b, g, r are the pins of onboard LED on tiny2040 which are "active low" - setting their value high to disable them. If you are using a different board you can comment out or delete these lines
b = machine.Pin(20, machine.Pin.OUT)
g = machine.Pin(19, machine.Pin.OUT)
r = machine.Pin(18, machine.Pin.OUT)
b.value(1)
g.value(1)
r.value(1)

# Defining our Analog to Digital bus
input_sens = machine.ADC(0)

# Defining PWM outputs, use as few or as many as you need.
led_output = machine.PWM(machine.Pin(29))
led_output2 = machine.PWM(machine.Pin(2))

# PWM Frequency
led_output.freq(5000)

# Variables, tweak as needed depending on your components.
sleep_time = 15
duty = 10
max_duty = 20000
input_sensitivity = 20000
active = False

# function to set duty on multiple pins simultaneously, add your pins here
def setDuty(duty):
    led_output.duty_u16(int(duty))
    led_output2.duty_u16(int(duty))

while True:
    
    # cycle starts at zero duty
    setDuty(0)
    
    #if the light level is below the threshold defined in input_sensitvity, active set to true.
    if input_sens.read_u16() < input_sensitivity:
        active = True
    else:
        #active set to false, and cpu sleeps for predetermined time
        active = False
        time.sleep(sleep_time)
    
    #fade up
    while active:
        while duty < max_duty:
            duty = duty * 1.01
            setDuty(duty)
            time.sleep(0.01)
        
        time.sleep(0.3)
        
        #fade down
        while duty > 10:
            duty = duty * 0.99
            setDuty(duty)
            time.sleep(0.01)
           
        # checking light level at the end of the loop to enable the loop to be exited
        if input_sens.read_u16() > input_sensitivity:
            active = False
            setDuty(0)
