import piconzero as pz
import threading

light_status = 0
motor_direction = 'Stop'
motor_speed = 100


class lights(object):
    """ A class to control the lights """

    def __init__(self):
        pz.init()
        # 1= 2 place, 1 = PWM output channel
        pz.setOutputConfig(1, 1)
        # 2= 3 place, 1 = PWM output channel
        pz.setOutputConfig(2, 1)
        # Set initial state as off
        pz.setOutput(1, 0)
        pz.setOutput(2, 0)
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def read_led(self):
        global light_status
        """ Read the state of the lights """
        with self._lock:
            return light_status

    def set_led(self, value):
        global light_status
        if value is True:
            pz.setOutput(1, 100)
            pz.setOutput(2, 100)
            light_status = 1
        else:
            pz.setOutput(1, 0)
            pz.setOutput(2, 0)
            light_status = 0


class motors():
    """ A class to control the motors """

    def __init__(self):
        pz.init()
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def read_direction(self):
        """ read the global variable motor_direction """
        global motor_direction
        with self._lock:
            return motor_direction

    def forward(self):
        """ Move both motors forward """
        global motor_speed
        global motor_direction
        with self._lock:
            # pz.forward(speed)
            pz.forward(motor_speed)
            motor_direction = 'Forward'
            return motor_direction

    def stop(self):
        global motor_direction
        with self._lock:
            pz.stop()
            motor_direction = 'Stop'
            return motor_direction
