from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^main/?', views.index),
    url(r'^ema/?', views.ema),
]
