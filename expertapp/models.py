from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now

class expertTaskDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    expertTaskId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    custTaskId=models.IntegerField(default=0)
    taskName=models.TextField()
    taskDescription=models.TextField()
    taskCategory=models.CharField(max_length=100)
    taskSubCategory=models.CharField(max_length=100)
    taskAttachment1=models.URLField(blank=True)
    taskAttachment2=models.URLField(blank=True)
    taskStatus=models.CharField(max_length=100)
    creationTime=models.DateTimeField(default=now())
    lastUpdateTime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.custTaskId

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50,null=True,blank=True)
    dateOfBirth=models.DateTimeField(null=True,blank=True)
    MobileNo=models.IntegerField(max_length=20,null=True,blank=True)
    houseNo=models.CharField(max_length=50,null=True,blank=True)
    town=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    district=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    pin=models.IntegerField(max_length=50,null=True,blank=True)
    messenger=models.CharField(max_length=50,null=True,blank=True)
    website=models.URLField(blank=True)
    bankName = models.CharField(max_length=200, null=True, blank=True)
    accountNo = models.CharField(max_length=200, null=True, blank=True)
    ifscCode = models.CharField(max_length=200, null=True, blank=True)
    swift = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    isAccountVerified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'



