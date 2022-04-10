from django.urls import path
from django.urls import include
from streamapp import views

from .views import KinesisView

app_name = 'streaming'

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', KinesisView.as_view(), name='video_feed')

]
