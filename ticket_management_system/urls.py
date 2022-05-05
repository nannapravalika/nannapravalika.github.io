"""ticket_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp import views as admin_views
from userapp import views as user_views
from mainapp import views as main_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #main
    path('',main_views.index,name='index'),
    path('admin-login',main_views.adminlogin,name="admin-login"),
    #user
    path('user-login',user_views.user_login,name="user-login"),
    path('user-registration',user_views.user_registration,name="user-registration"),
    path('user-home',user_views.user_home,name="user-home"),
    path('user-booking-status',user_views.user_booking_status,name="user-booking-status"),
    path('user-raise-complaints/<int:id>/',user_views.user_raise_complaints,name="user-raise-complaints"),
    #admin
    path('admin-home',admin_views.admin_home,name="admin-dashboard"),
    path('admin-complaints',admin_views.admin_complaints,name="admin-complaints"),
    path('admin-tickets-raised',admin_views.admin_tickets_raised,name="admin-tickets-raised"),
    path('accept-booking/<int:id>/',admin_views.accept_ticket,name="accept-booking"),
    path('reject-booking/<int:id>/',admin_views.reject_ticket,name="reject-booking"),
    
]
