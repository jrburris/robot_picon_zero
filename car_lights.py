import piconzero as pz


class lights(object):
    """ A class to control thee lights """

    def __init__(self):
        # pz.init()
        # 1= 2 place, 1 = PWM output channel
        pz.setOutputConfig(1, 1)
        # 2= 3 place, 1 = PWM output channel
        pz.setOutputConfig(2, 1)

    def read_lights(self):
        """ Read the state of the lights """
        return 0

    def set_led(self, value):
        if value > 0:
            pz.setOutput(1, value)
            pz.setOutput(2, value)
        else:
            pz.setOutput(1, 0)
            pz.setOutput(2, 0)
