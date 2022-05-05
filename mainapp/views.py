from django.shortcuts import render, redirect
from adminapp.views import *

# Create your views here.
def index(request):
    print("ok")
    return render(request,'main/index.html')

def adminlogin(request):
    if request.method == "POST":
        name = request.POST.get('Username')
        password =request.POST.get('Password')
        if name =='admin' and password =='admin':
            return redirect ("admin-dashboard")
        else :
            print ('invalid')    
    return render (request,'main/admin-login.html')