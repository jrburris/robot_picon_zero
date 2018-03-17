import time
import picon


lights = picon.lights()

# current light status
status = lights.read_led()
print('Lights status is: {}'.format(status))

print('Blinking LED (Ctrl-C to stop)...')
while True:

    lights.set_led(0)
    time.sleep(1)
    status = lights.read_led()
    print('Lights status is: {}'.format(status))

    lights.set_led(100)
    time.sleep(1)
    status = lights.read_led()
    print('Lights status is: {}'.format(status))
