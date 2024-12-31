from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('text/',views.chat_room,name='text'),
    path('clear/',views.clear,name='clear'),
    path('register/',views.register,name='register')
    
    


]
