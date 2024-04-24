#!/usr/bin/env python3

from django.urls import path

from . import views

app_name = "bot"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
