from django.urls import path
from django.urls import include
from streamapp import views

app_name = 'streaming'

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    # path('video_feed', views.video_feed, name='video_feed'),  # laptop
    # path('webcam_feed', views.webcam_feed, name='webcam_feed'),  # mobile

]
