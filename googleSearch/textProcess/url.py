
from django.conf.urls import url,include
from django.contrib import admin
from .views import *


urlpatterns = [
    url('',teste.as_view(),name='teste'),
]
