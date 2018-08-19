from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^new/$', views.new),   # This line has changed!
    url(r'^create/$', views.create)   # This line has changed!
]
