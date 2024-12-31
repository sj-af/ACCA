from django.shortcuts import render,redirect
from .models import Login,room
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'acca.html')

def login(request):
    if request.POST:
        uname=request.POST['uname']
        pword=request.POST['pword']
        s=Login.objects.filter(username=uname,password=pword)
       
        if s:
            request.session['id']=s[0].id
           
            return redirect('text')
        
    return render(request,'home.html')
        


def chat_room(request):
    return render(request, 'text.html')

def clear(request):
    room.objects.all().delete()

    return redirect('home')


def register(request):
    if request.POST:
        uname=request.POST['uname']
        pword=request.POST['pword']
        Login.objects.create(username=uname,password=pword)
       
  
        
    return render(request,'register.html')




