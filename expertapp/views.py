from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
import dateutil.parser
from .models import *
import logging
logger=logging.getLogger(__name__)

# Create your views here.

def home(request):
    return render(request,'expertapp/home.html')

def expertHome(request):
    return render(request,'expertapp/experthome.html')

class getTaskDetails(APIView):
    def post(self,request):
        ser=getTaskDetailsSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            logger.info(ser.data)
            return Response(ser.data,status=200)
        logger.info(ser.errors)
        return Response(ser.errors,status=400)


def registerPage(request):
    form = RegistrationForm(request.POST)
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request,'expertapp/register.html',context=context)

@login_required()
def expertDashBoard(request):
    user_id=request.user.id
    query=expertTaskDetails.objects.filter(user_id=user_id).order_by('-custTaskId')
    context={'taskdata':query}
    return render(request,'expertapp/dashboard.html',context)

@login_required()
def profileView(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        dateOfBirth = request.POST.get('dob')
        gender = request.POST.get('gender')
        MobileNo = request.POST.get('mobile')
        website = request.POST.get('website')
        houseNo = request.POST.get('houseNo')
        town=request.POST.get('town')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        bankName=request.POST.get('name')
        accountNo=request.POST.get('accountNo')
        ifscCode = request.POST.get('ifsc')
        swift = request.POST.get('swift')
        iban = request.POST.get('iban')



        if first_name:
            request.user.first_name=first_name
            request.user.save()
        if last_name:
            request.user.last_name=last_name
            request.user.save()
        if dateOfBirth:
            request.user.profile.dateOfBirth=dateutil.parser.parse(dateOfBirth)
            request.user.profile.save()
        if gender:
            request.user.profile.gender=gender
            request.user.profile.save()
        if MobileNo:
            request.user.profile.MobileNo=MobileNo
            request.user.profile.save()
        if website:
            request.user.profile.website = website
            request.user.profile.save()
        if houseNo:
            request.user.profile.houseNo=houseNo
            request.user.profile.save()
        if town:
            request.user.profile.town=town
            request.user.profile.save()
        if city:
            request.user.profile.city=city
            request.user.profile.save()
        if district:
            request.user.profile.district = district
            request.user.profile.save()
        if state:
            request.user.profile.state=state
            request.user.profile.save()
        if pin:
            request.user.profile.pin=pin
            request.user.profile.save()
        if bankName:
            request.user.profile.bankName = bankName
            request.user.profile.save()
        if accountNo:
            request.user.profile.accountNo = accountNo
            request.user.profile.save()
        if ifscCode:
            request.user.profile.ifscCode = ifscCode
            request.user.profile.save()
        if swift:
            request.user.profile.swift = swift
            request.user.profile.save()
        if iban:
            request.user.profile.iban = iban
            request.user.profile.save()


    userdata=User.objects.filter(id=request.user.id)[0]
    profileData=Profile.objects.filter(id=request.user.profile.id)[0]

    context = {'userdata': userdata,'profileData':profileData}
    return render(request,'expertapp/profile.html',context=context)

