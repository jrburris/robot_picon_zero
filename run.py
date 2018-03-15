from flask import Flask
from flask import render_template

import psutil
import picon


app = Flask(__name__)

speed = 100
direction = 'Stop'

# Initialize pico bits
lights = picon.lights()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/robot")
def robot():

    headlights = lights.read_led()
    return render_template('robot.html', headlights=headlights,
                           direction=direction)


@app.route("/robot/headlights/<int:brightness>", methods=['POST'])
def headlights(brightness):
    if brightness <= 100:
        lights.set_led(brightness)
    else:
        return ('Error: LED brightness, should be 0 to 100', 400)
    return ('', 204)


@app.route("/forward")
def forward():
    pz.forward(speed)
    print 'Forward', speed
    direction = "Forward"
    return 'true'


@app.route("/reverse")
def reverse():
    pz.reverse(speed)
    print 'Reverse', speed
    direction = 'Reverse'
    return 'true'


@app.route("/right")
def right():
    pz.spinLeft(speed)
    print 'Spin Right', speed
    direction = 'Spin Right'
    return 'true'


@app.route("/left")
def left():
    pz.spinRight(speed)
    print 'Spin Left', speed
    direction = 'Spin Left'
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
