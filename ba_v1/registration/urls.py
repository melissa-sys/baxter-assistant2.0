from django.urls import path
from .views import SignUpView

app_name = 'registration'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'registro')
]
