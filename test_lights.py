import time

from car_lights import lights

lights = lights()

# current light status
status = lights.read_lights()
print('Lights are {}'.format(status))

print('Blinking LED (Ctrl-C to stop)...')
while True:
    lights.set_led(0)
    time.sleep(0.5)

    print("lights at 20")
    lights.set_led(20)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)

    print("lights at 40")
    lights.set_led(40)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)

    print("lights at 60")
    lights.set_led(60)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)

    print("lights at 80")
    lights.set_led(80)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)

    print("lights at 100")
    lights.set_led(100)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)

    print("lights at 120")
    lights.set_led(120)
    time.sleep(4)
    lights.set_led(0)
    time.sleep(1)
