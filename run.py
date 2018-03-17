from flask import Flask
from flask import render_template, Response

import time
import psutil
import picon


app = Flask(__name__)

speed = 100
direction = 'Stop'

# Initialize pico bits
lights = picon.lights()


@app.route("/robot")
def robot():
    headlights = lights.read_led()
    return render_template('robot.html', headlights=headlights,
                           direction=direction)


@app.route("/robot/headlights/<int:state>", methods=['POST'])
def set_headlights(state):
    if state == 1:
        lights.set_led(True)
    elif state == 0:
        lights.set_led(False)
    else:
        return ('Error: LED state, should be 0 or 1', 400)
    return ('', 204)


@app.route("/robot/headlights")
def get_headlights():
    def read_headlights():
        while True:
            headlights = lights.read_led()
            yield 'data: {0}\n\n'.format(headlights)
            time.sleep(1.0)
    return Response(read_headlights(), mimetype='text/event-stream')


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


@app.route('/stop')
def stop():
    pz.stop()
    print 'Stop'
    return 'true'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5010, threaded=True)
