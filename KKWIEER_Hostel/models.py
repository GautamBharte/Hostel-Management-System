from sre_constants import CATEGORY
from django.db import models

# Create your models here.

class Student(models.Model):
    prn = models.CharField(max_length=12, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=50, null=True)
    room_no = models.CharField(max_length=5, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Complaint(models.Model):
    CATEGORY = (
        ('Hostel Problem', 'Hostel Problem'),
        ('Mess Problem', 'Mess Problem'),
        ('Ragging Case', 'Ragging Case'),
        ('Fees Issue', 'Fees Issue')
    )
    # category =
    # title = 
    date_created = models.DateTimeField(auto_now_add=True)