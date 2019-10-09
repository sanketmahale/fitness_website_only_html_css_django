from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request,'trainers.html',{'trainers':trainers})
def signup(request):
    if request.method == 'POST' : 
        name = request.POST['Name']
        email = request.POST['email']
        password = request.POST['password'] 
        plan = request.POST.get('plan')
        user = User.objects.create_user(username=name,password=password,email=email)
        user.save()
        position = 'customer'
        profile = Profile.objects.create(position = position)
        profile.save()
        print("User created")
        return redirect('/')
    else:
        return render(request,'signup.html')
def recepies(request):
    meals = Meals.objects.all()
    return render(request,'recepies.html',{'meals':meals})
