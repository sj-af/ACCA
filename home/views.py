from django.shortcuts import render,redirect
from .models import Login,room
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods



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
        

@login_required(login_url='login/')
def text(request):
    pk = request.session.get('id')
    
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            room.objects.create(user=pk, text=text)
    
    texts1 = room.objects.all()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [{'user': message.user, 'text': message.text} for message in texts1]
        return JsonResponse({'texts1': data})

def clear(request):
    room.objects.all().delete()

    return redirect('home')


def register(request):
    if request.POST:
        uname=request.POST['uname']
        pword=request.POST['pword']
        Login.objects.create(username=uname,password=pword)
       
  
        
    return render(request,'register.html')




