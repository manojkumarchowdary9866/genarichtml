from django.urls import path
from app18.views import app18
app_name='app18'
urlpatterns=[
    path('app18/',app18,name='app18'),
]
