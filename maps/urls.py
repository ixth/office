from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.map, name='map'),
    url(r'^(?P<pk>\d+)/tiles/(?P<z>\d+)/tile-(?P<x>\d+)-(?P<y>\d+).png$', views.tile, name='tile'),
]
