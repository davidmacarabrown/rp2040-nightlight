from machine import Pin, PWM, ADC
import time

b = machine.Pin(20, machine.Pin.OUT)
g = machine.Pin(19, machine.Pin.OUT)
r = machine.Pin(18, machine.Pin.OUT)

b.value(1)
g.value(1)
r.value(1)

input_sens = machine.ADC(0)

led_output = machine.PWM(machine.Pin(29))
led_output2 = machine.PWM(machine.Pin(2))

led_output.freq(5000)

sleep_time = 15
duty = 10
max_duty = 20000
input_sensitivity = 20000
active = False

def setDuty(duty):
    led_output.duty_u16(int(duty))
    led_output2.duty_u16(int(duty))

while True:
    setDuty(0)
    
    if input_sens.read_u16() < input_sensitivity:
        active = True
    else:
        active = False
        time.sleep(sleep_time)
    
    while active:
        while duty < max_duty:
            duty = duty * 1.01
            setDuty(duty)
            time.sleep(0.01)
        
        time.sleep(0.3)
        
        while duty > 10:
            duty = duty * 0.99
            setDuty(duty)
            time.sleep(0.01)
            
        if input_sens.read_u16() > input_sensitivity:
            active = False
            setDuty(0)