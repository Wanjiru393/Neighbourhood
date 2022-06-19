from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin,logout

from .models import neighbourhood,healthservices,Business,Health,Authorities,notifications
from .forms import notificationsForm,ProfileForm,BusinessForm,RegisterForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


def login(request):	
   print(request.method)
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      print(username, password)
      try:
         user = User.objects.get(username=username, password=password)

      except:
         messages.error(request, 'Invalid username or password')

      user = authenticate(request, username=username, password=password)
      if user is not None:
         authlogin(request,user)
         return redirect('index')
      else:
         messages.error(request, 'Invalid username or password')

   return render(request, 'login.html') 

def register(request):
   register_form = RegisterForm()
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.save()
         profile = Profile(username=username)
         profile.save()

      return redirect('login')
   context = {
      'form': register_form,
   }

   return render(request, 'register.html', context)


def logout(request):
   return redirect('login')


def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')

@login_required(login_url='login/')
def notification(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'notifications.html',{"notifications":all_notifications})


@login_required(login_url='login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'businesses.html',{"businesses":businesses})


@login_required(login_url='login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'health.html',{"healthservices":healthservices})

