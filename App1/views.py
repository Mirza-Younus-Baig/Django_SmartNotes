from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse('This is the home page!')

def default(request):
    return HttpResponse('This is the default page')

def currentTime(request):
    ct = datetime.now()
    return render(request, 'App1/currentTime.html', {'currentTime': ct})

@login_required(login_url='admin/')
def authCheck(request):
    return render(request, 'App1/authCheck.html', {})