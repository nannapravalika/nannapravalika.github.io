from datetime import date
from django.shortcuts import redirect, render,get_object_or_404
from userapp.models import UserBookTicketModel,UserComplaintModel,UserRegModel

# Create your views here.
def admin_home(request):
    users=UserRegModel.objects.all().count()
    bookings=UserBookTicketModel.objects.all().count()
    complaints=UserComplaintModel.objects.all().count()
    return render(request,'admin/admin-dashboard.html',{'users':users,'bookings':bookings,'complaints':complaints})

def admin_tickets_raised(request):
    tickets=UserBookTicketModel.objects.all()
    return render(request,'admin/admin-tickets-raised.html',{'tickets':tickets})

def accept_ticket(request,id):
    object = get_object_or_404(UserBookTicketModel,booking_id=id)
    object.status="Accepted"
    object.save(update_fields=["status"])
    return redirect('admin-tickets-raised')

def reject_ticket(request,id):
    object = get_object_or_404(UserBookTicketModel,booking_id=id)
    object.status="Rejected"
    object.save(update_fields=["status"])
    return redirect('admin-tickets-raised')

def admin_complaints(request):
    complaint=UserComplaintModel.objects.all()
    return render(request,'admin/admin-complaints.html',{'complaint':complaint})

