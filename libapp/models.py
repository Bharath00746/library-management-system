from django.db import models

# Create your models here.

class user_signup(models.Model):
    Name=models.CharField(max_length=100)
    Dob=models.DateField()
    Email=models.CharField(max_length=100)
    Mob=models.BigIntegerField()
    Password=models.CharField(max_length=20)
    status=models.IntegerField(default=1)
    

class Book_details(models.Model):
    Book_Name=models.CharField(max_length=50)
    Book_code=models.CharField(max_length=10)
    Author_Name=models.CharField(max_length=50)
    Date=models.DateField()
    Status=models.CharField(max_length=50)
    Book_Amount=models.IntegerField()
    Created_Date=models.DateField()
    Created_By=models.CharField(max_length=50)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=50)
    Book_Img=models.FileField(upload_to='image')