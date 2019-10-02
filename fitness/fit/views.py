from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request,'login.html')
def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    return render(request,'trainers.html')
