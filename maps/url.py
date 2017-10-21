from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tiles/(?P<z>\d+)/(?P<y>\d+)/(?P<x>\d+).png$', views.tile, name='tile'),
]
