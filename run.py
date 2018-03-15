from flask import Flask
from flask import render_template

import psutil
import time
import piconzero as pz

app = Flask(__name__)

speed = 100


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/robot")
def robot():
    return render_template('robot.html')


@app.route("robot/lights_on")
def lights_on():
    pz.init()
    pz.setOutputConfig(1, 1)
    pz.setOutputConfig(2, 1)

    pz.setOutput(1, 100)
    pz.setOutput(2, 100)

    # while True:
    #     pz.setOutput(1, 5)
    #     pz.setOutput(2, 5)
    #     # 5% - very dim
    #     time.sleep(1)
    #     pz.setOutput(1, 30)
    #     pz.setOutput(2, 30)
    #     # 30% - medium
    #     time.sleep(1)
    #     pz.setOutput(1, 70)
    #     pz.setOutput(2, 70)
    #     # 70% - bright
    #     time.sleep(1)
    #     pz.setOutput(1, 100)
    #     pz.setOutput(2, 100)
    #     # 100% - maximum
    #     time.sleep(1)
    return 'lights on'


@app.route("/lights_off")
def lights_off():
    pz.setOutput(1, 0)
    pz.setOutput(2, 0)

    return 'lights off'


@app.route("/forward")
def forward():
    pz.forward(speed)
    print 'Forward', speed
    return 'true'


@app.route("/reverse")
def reverse():
    pz.reverse(speed)
    print 'Reverse', speed
    return 'true'


@app.route("/right")
def right():
    pz.spinLeft(speed)
    print 'Spin Right', speed
    return 'true'


@app.route("/left")
def left():
    pz.spinRight(speed)
    print 'Spin Left', speed
    return 'true'


@app.route("/cpu")
def getCpu():
    print("CPU: {}".format(psutil.cpu_percent()))
    #  physical memory usage
    # svmem(total=388681728,
    # available=228765696,
    # percent=41.1,
    # used=104443904,
    # free=74240000,
    # active=179245056,

    print('Memory Available: {}'.format(psutil.virtual_memory().available))
    print('Memory Used: {}'.format(psutil.virtual_memory().used))

    return ''

# elif keyp == '.' or keyp == '>':
#     speed = min(100, speed + 10)
#     print 'Speed+', speed
# elif keyp == ',' or keyp == '<':
#     speed = max(0, speed - 10)
#     print 'Speed-', speed


@app.route('/stop')
def stop():
    pz.stop()
    print 'Stop'
    return 'true'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5010)
