from django.urls import path # type: ignore
from app2.views import *
urlpatterns=[
    path('app12/',app12,name='app12') # type: ignore
]