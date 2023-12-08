from msd.views import *
from django.urls import path
app_name='special'
urlpatterns=[
    path('appmsd/',appmsd,name='appmsd'),
]