from django.shortcuts import render,redirect
from .models import Login,room
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


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
        


def text(request):
    pk = request.session.get('id')  # Retrieve user id from session
    
    if request.method == 'POST':
        text = request.POST.get('text')
        
        if text:  # If there is text in the message
            room.objects.create(user=pk, text=text)
    
    # Fetch all messages from the room
    texts1 = room.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [{'user': message.user, 'text': message.text} for message in texts1]
        return JsonResponse({'texts1': data})
    
    # If the request is for a normal page load, render the page with the messages
    return render(request, 'text.html', {'texts1': texts1, 'id': pk})

# New view to handle typing status
def typing_status(request):
    if request.method == 'POST':
        typing_status = request.POST.get('typing')  # Get typing status
        user_id = request.session.get('id')

        if typing_status == 'true':
            # Save that the user is typing (you can store this in a cache, session, or database)
            request.session['typing'] = True
        else:
            # Clear the typing status when the user stops typing
            request.session['typing'] = False
        
        return JsonResponse({'status': 'success'})

def clear(request):
    room.objects.all().delete()

    return redirect('home')


def register(request):
    if request.POST:
        uname=request.POST['uname']
        pword=request.POST['pword']
        Login.objects.create(username=uname,password=pword)
       
  
        
    return render(request,'register.html')




