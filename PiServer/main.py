from flask import Flask, render_template, Response, request, send_from_directory

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from camera import VideoCamera
from gpiozero import Robot

import time
import threading
import os

users = {
    "rajeevan": generate_password_hash("865865")
}

pi_camera = VideoCamera(flip=False)
robo_car = Robot((17, 27), (10, 9))

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
@auth.login_required
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/robot')
@auth.login_required
def robot():
    args = request.args
    speed = min(max(float(args.get('speed')), -1), 1)
    direction = min(max(float(args.get('direction')), -1), 1)

    curve_left = 0
    curve_right = 0
    if direction > 0:
        curve_right = direction
    elif direction < 0:
        curve_left = -1 * direction
    else:
        curve_right = 0
        curve_left = 0

    print('Speed: ', speed)
    print('Curve Left: ', curve_left)
    print('Curve Right: ', curve_right)

    if speed > 0:
        robo_car.forward(speed=speed, curve_right=curve_right, curve_left=curve_left)
    elif speed < 0:
        robo_car.forward(speed=-1 * speed, curve_right=curve_right, curve_left=curve_left)
    else:
        robo_car.stop()
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, ssl_context=('cert.pem', 'key.pem'))
