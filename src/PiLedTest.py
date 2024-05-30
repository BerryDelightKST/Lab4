import hal.hal_led as led
import hal.hal_input_switch as switch
from time import sleep

led.init()
switch.init()
def LedBlinker(starto):
    if starto==1:
        led.set_output(led,True)
        sleep(0.2)
        led.set_output(led,False)
        sleep(0.2)
    elif starto==0:
        for x in range (50):
            led.set_output(led,True)
            sleep(0.1)
            led.set_output(led,False)
            sleep(0.1)
            print (x)
            if x == 49:
                return 0

            

while True:
    starto=switch.read_slide_switch()
    stopper=LedBlinker(starto)
    while stopper==0:
        led.set_output(led,False)
        stopper=switch.read_slide_switch()
        
        