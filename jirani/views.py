from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin,logout

from .models import neighbourhood,healthservices,Business,Health,Authorities,notifications,Profile
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
         profile = Profile(username=user.id)
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
            return redirect('')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')


@login_required(login_url='/accounts/login/')
def notification(request):
    # curent_user= request.user
    profile=Profile.objects.get(username=request.user.id)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood).all()

    return render(request,'notifications.html',{"notifications":all_notifications})

@login_required(login_url='')
def health(request):
    # current_user=request.user
    profile=Profile.objects.get(username=request.user.id)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood).all()

    return render(request,'health.html',{"healthservices":healthservices})


@login_required(login_url='')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'authorities.html',{"authorities":authorities})


@login_required(login_url='')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'businesses.html',{"businesses":businesses})

@login_required(login_url='')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'user_profile.html',{"profile":profile})


@login_required(login_url='')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

    return render(request,'user_profile.html',{"profile":profile})



@login_required(login_url='')
def new_business(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'new_business.html',{"form":form})


@login_required(login_url='')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('index')

    else:

        form = ProfileForm()
    return render(request,'create_profile.html',{"form":form})


@login_required(login_url='')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})


@login_required(login_url='')
def new_notification(request):
    # current_user=request.user
    # profile =Profile.objects.get(username=current_user.id)

    if request.method=="POST":
        form =notificationsForm(request.POST,request.FILES)
        if form.is_valid():
            notification = form.save(commit = False)
            notification.author = request.user
            # notification.neighbourhood = profile.neighbourhood
            notification.save()

        return HttpResponseRedirect('/notifications')

    else:
        form = notificationsForm()

    return render(request,'new_notifications.html',{"form":form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message=f"{search_term}"

        print(searched_businesses)

        return render(request,'search.html',{"message":message,"blogs":searched_businesses})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})
