from django.db import models
from adminapp import *

# Create your models here.
class UserRegModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100,help_text='Enter First name')
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100,help_text='Enter email')
    password=models.CharField(max_length=100,help_text='Enter Password')
    
    class Meta:
        db_table='user_details'
        
class UserBookTicketModel(models.Model):
    booking_id=models.AutoField(primary_key=True)
    user_details=models.ForeignKey(UserRegModel,db_column="user",on_delete=models.CASCADE,related_name='user')        
    book_from=models.CharField(max_length=100)
    book_to=models.CharField(max_length=100)
    date=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=100,null=True)
    no_of_adults=models.IntegerField()
    no_of_children=models.IntegerField()
    train_number=models.IntegerField()
    train_name=models.CharField(max_length=100)
    status=models.CharField(default="pending",max_length=100)
    
    class Meta:
        db_table='booking_details'

class UserComplaintModel(models.Model):
    complaint_id=models.AutoField(primary_key=100)
    train=models.ForeignKey(UserBookTicketModel,db_column="train",on_delete=models.CASCADE) 
    
    complaint=models.TextField()
    
    class Meta:
            db_table='user_complaints' 
    