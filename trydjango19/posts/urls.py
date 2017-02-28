from django.conf.urls import url
from django.contrib import admin

from posts import views

urlpatterns = [
  	url(r'^$', views.post_home),
]