from django.urls import path # type: ignore
from app1.views import * # type: ignore
urlpatterns=[
    path('app11/',app11,name='app11') # type: ignore
]