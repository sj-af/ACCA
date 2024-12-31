from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('chat_room/',views.chat_room,name='chat_room'),
    path('clear/',views.clear,name='clear'),
    path('register/',views.register,name='register')
    
    


]
