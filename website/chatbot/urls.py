# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("website/chatbot/", views.chat, name="chat"),
]