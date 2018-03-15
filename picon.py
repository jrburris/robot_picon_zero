import piconzero as pz

light_status = 0


class lights(object):
    """ A class to control thee lights """

    def __init__(self):
        pz.init()
        # 1= 2 place, 1 = PWM output channel
        pz.setOutputConfig(1, 1)
        # 2= 3 place, 1 = PWM output channel
        pz.setOutputConfig(2, 1)
        # Set initial state as off
        pz.setOutput(1, 0)
        pz.setOutput(2, 0)

    def read_led(self):
        global light_status
        """ Read the state of the lights """
        return light_status

    def set_led(self, value):
        global light_status
        if value > 0:
            pz.setOutput(1, value)
            pz.setOutput(2, value)

        else:
            pz.setOutput(1, 0)
            pz.setOutput(2, 0)

        light_status = value
