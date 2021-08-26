#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response
import cv2

import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    os.system(
        "DEL /F/Q/S \"C:\\Users\\kingr\\Videos\\iVCam\"")

    return render_template('index2.html')


@app.route('/detection')
def detection():
    os.system(
        "xcopy \"C:\\Users\\kingr\\Videos\\iVCam\\*.*\" \"D:\\ray\\1\\static\\1\\\" /s /e /y /i")
    path = 'C:/Users/kingr/Videos/iVCam/'
    all = os.listdir(path)
    file_list = []
    for f in all:
        path_one = f"/static/1/{f}"
        file_list.append(path_one)
        print(path_one)
    return render_template('detection.html', hists=file_list)


@app.route('/pic')
def pic():
    path = 'C:/Users/kingr/Videos/iVCam/'
    all = os.listdir(path)
    for f in all:
        if f == 'cut':
            continue
        print(f)

    return render_template('index3.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
