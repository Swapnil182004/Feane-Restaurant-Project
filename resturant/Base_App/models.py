from django.db import models
import datetime


# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.Category_name   #This func is for showing items on admin panel as name not as objects
    

class Items(models.Model):
    Item_name = models.CharField(max_length=25)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="items/")

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    About_Description = models.TextField(blank=False)

class BookTable(models.Model):
    Name = models.CharField(max_length=30)
    Phone_Number = models.IntegerField()
    Email = models.EmailField()
    Total_Person = models.IntegerField()
    Booking_Date = models.DateField(auto_now=False, auto_now_add=False)

    # New Fields with default values
    Booking_Time = models.TimeField(default=datetime.time(19, 0))  # Default time 19:00 (7 PM)
    Cab_Required = models.BooleanField(default=False)
    Pickup_Location = models.CharField(max_length=255, blank=True, null=True)
    Pickup_Coordinates = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.Name} - {self.Booking_Date} {self.Booking_Time}"


class Feedback(models.Model):
    User_Name = models.CharField(max_length=30)
    Feedback_Description = models.TextField(max_length=55, blank=False)
    Rating = models.IntegerField()
    User_Image = models.ImageField(upload_to="items/", blank=True)

    def __str__(self):
        return self.User_Name