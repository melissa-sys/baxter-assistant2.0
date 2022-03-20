from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
from streamapp.camera import IPWebCam

# Create your views here.

# Pintar el html donde saldrá el video


def index(request):
    return render(request, 'streamapp/home_video.html')

# Creamos un método para la cámara que se vaya a utilizar


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    pass
    # return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary= frame')


# def webcam_feed(request):
#     return StreamingHttpResponse(gen(IPWebCam()), content_type='multipart/x-mixed-replace; boundary= frame')
