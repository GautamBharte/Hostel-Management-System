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
    STATUS = (
        ('Pending', 'Pending'),
        ('Viewed', 'Viewed'),
        ('Completed', 'Completed')
    )
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    title = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__(self) -> str:
        return self.student.name + '(' + self.category + ')'