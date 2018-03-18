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
motors = picon.motors()


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


@app.route("/robot/direction")
def get_direction():
    def read_direction():
        while True:
            direction = motors.read_direction()
            yield 'data: {0}\n\n'.format(direction)
            time.sleep(1.0)
    return Response(read_direction(), mimetype='text/event-stream')


@app.route("/robot/forward")
def go_forward():
    motors.forward()
    return ('', 204)


@app.route("/robot/reverse")
def go_reverse():
    motors.reverse()
    return ('', 204)


@app.route("/robot/stop")
def stop():
    motors.stop()
    return ('', 204)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5010, threaded=True)
