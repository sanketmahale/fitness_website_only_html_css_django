from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None : 
            auth.login(request,user)
            Profiles = Profile.objects.all()
            print(user.pk)
            for p in Profiles :
                print(p.user_id)
                if(user.pk==p.user_id):
                    position = p.position
            if(position == "customer"):
                return redirect('/')
            if(position == "trainer"):
                return redirect('/')
        else :
            return redirect('/')
    else:
        return render(request,'login.html')

def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request,'trainers.html',{'trainers':trainers})
def signup(request):
    if request.method == 'POST' : 
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=name,password=password,email=email)
        user.save()
        position = 'customer'
        profile = Profile.objects.create(user=user,position = position)
        profile.save()
        print("User created")
        return redirect('pay')
    else:
        return render(request,'signup.html')
def recepies(request):
    meals = Meals.objects.all()
    return render(request,'recepies.html',{'meals':meals})

def pay(request):
    if(request.method=="POST"):
        name = request.POST['name']
        plan = request.POST.get('plan')
        category = request.POST.get('category')
        cats = Meals.objects.all()
        for cat in cats:
            if(cat.name==category):
                mealId = cat 
        trainers = Trainer.objects.all()
        for trainer in trainers :
            if(trainer.type.name==category):
                train = trainer

        customer = Customer.objects.create(name=name,pricing=plan,trainerId=train,mealId=mealId)
        return redirect('/')
    else:    
        plans = Meals.objects.all()
        return render(request,'pay.html',{'plans':plans})

def logout(request):
    auth.logout(request)
    return redirect('/')