import hal.hal_led as led
import hal.hal_input_switch as switch
from time import sleep

led.init()
switch.init()
def LedBlinker():
    isOn=switch.read_slide_switch()
    if isOn==True:
        led.set_output(led,True)
        sleep(0.2)
        led.set_output(led,False)
        sleep(0.2)
    else:
        led.set_output(led,True)
        sleep(0.1)
        led.set_output(led,False)
        sleep(0.1)
        

while True:
    LedBlinker()