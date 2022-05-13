from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .models import UserBookTicketModel,UserComplaintModel,UserRegModel 

# Create your views here.
def user_login(request):
    if request.method=="POST":
        print("valid")
        name = request.POST.get('Email')
        password =request.POST.get('Password')
        
        try:
           check=UserRegModel.objects.get(email=name,password=password)
           request.session["user_id"]=check.user_id
           return redirect ('user-home')
        except: 
            messages.error(request, "Message sent." )
    return render(request,'user/user-login.html')

def user_registration(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        UserRegModel.objects.create(full_name=fname,email=email,mobile=mobile,password=password)
        messages.success(request, "Message sent." )
    return render(request,'user/user-registration.html')

def user_home(request):
    user_id=request.session["user_id"]
    if request.method=="POST":
        book_from=request.POST.get('from')
        book_to=request.POST.get('to')
        adults=request.POST.get('adults')
        child=request.POST.get('child')
        train_number=request.POST.get('train_number')
        train_name=request.POST.get('train_name')
        user=UserRegModel.objects.filter(user_id=user_id).first()
        
        UserBookTicketModel.objects.create(user_details=user,book_from=book_from,book_to=book_to,no_of_adults=adults,no_of_children=child,train_number=train_number,train_name=train_name)
        messages.success(request, "Message sent." )
    return render(request,'user/user-home.html')

def user_booking_status(request):
    user_id=request.session["user_id"]
    tickets=UserBookTicketModel.objects.filter(user_details=user_id)
    complaint=UserComplaintModel.objects.filter(train=user_id)
    return render (request,'user/user-booking-status.html',{'tickets':tickets,'complaint':complaint})

def user_raise_complaints(request,id):
    user_id=request.session["user_id"]
    if request.method=="POST":
        complaint=request.POST.get("Complaint")
        train=UserBookTicketModel.objects.filter(booking_id=id).first()
        user=UserRegModel.objects.filter(user_id=user_id).first()
        
        UserComplaintModel.objects.create(complaint=complaint,train=train,user=user)
        
    return render(request,'user/user-raise-complaints.html')

def user_view_complaints(request):
    user_id=request.session["user_id"]
    complaints=UserComplaintModel.objects.filter(user=user_id)
    return render(request,'user/user-view-complaints.html',{'complaints':complaints})

def user_edit_complaints(request,id):
    complaints=UserComplaintModel.objects.filter(complaint_id=id)
    if request.method=="POST":
        obj=get_object_or_404(UserComplaintModel,complaint_id=id)
        obj.complaint=request.POST.get("complaint")
        obj.save()
        
    return render(request,'user/user-edit-complaints.html',{'complaints':complaints})