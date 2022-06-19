from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

def index(request):
   
    return render(request,'index.html')


