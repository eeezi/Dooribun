from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_index, name='chat_index'),
    #path('room/', views.room, name='room'),
]