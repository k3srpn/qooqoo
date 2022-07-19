from django.db import models
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    reg_num = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    bank = models.CharField(max_length=20)
    bank_num = models.CharField(max_length=30)
    inwork = models.DateField()
    department = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    worksystem = models.IntegerField()
    pay = models.IntegerField()
    insurance = models.CharField(max_length=20)
    health = models.CharField(max_length=30)
    content = models.TextField()

class Parttimer(models.Model):
    name = models.CharField(max_length=30)
    reg_num = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    pay = models.IntegerField()
    bank = models.CharField(max_length=20)
    bank_num = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    part = models.CharField(max_length=30)
    inwork = models.DateField()
    outwork = models.DateField(null=True, blank=True)
    health = models.CharField(max_length=30)
    content = models.TextField()

class WorkEmployee(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    working = models.CharField(max_length=15)
    start = models.CharField(max_length=15)
    end = models.CharField(max_length=15)
    extra_type = models.CharField(max_length=10, blank=True, null=True)
    extra = models.IntegerField(blank=True, null=True)
    dayoff = models.IntegerField()
    annual = models.IntegerField()
    content = models.TextField()