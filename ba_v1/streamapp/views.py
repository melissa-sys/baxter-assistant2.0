from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import StreamingHttpResponse

import cv2
import socket
import numpy as np
import time
import base64
# from streamapp.camera import VideoCamera
# from streamapp.camera import IPWebCam

# Create your views here.

# Pintar el html donde saldrá el video


def index(request):
    return render(request, 'streamapp/home_video.html')

# Creamos un método para la cámara que se vaya a utilizar


class Video(object):
    def get_frame(self):
        BUFF_SIZE = 65536
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
        host_name = socket.gethostname()
        host_ip = '192.168.1.60'  # socket.gethostbyname(host_name)
        print(host_ip)
        port = 9999
        message = b'Hello'
        client_socket.sendto(message, (host_ip, port))
        fps, st, frames_to_count, cnt = (0, 0, 20, 0)

        while (True):
            # print('melos')
            packet, _ = client_socket.recvfrom(BUFF_SIZE)
            data = base64.b64decode(packet, ' /')
            npdata = np.fromstring(data, dtype=np.uint8)
            frame = cv2.imdecode(npdata, 1)
            cv2.imshow("RECEIVING VIDEO", frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            r = jpeg.tobytes()

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
                break
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + r + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(Video().get_frame(), content_type='multipart/x-mixed-replace; boundary= frame')


# def webcam_feed(request):
#     return StreamingHttpResponse(gen(IPWebCam()), content_type='multipart/x-mixed-replace; boundary= frame')
