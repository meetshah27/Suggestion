from datetime import *
from django.shortcuts import render
from django.shortcuts import HttpResponse
# from django.contrib import messages
# from .models import Police
# Create your views here.
from datetime import *
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Suggestion_Data
# from rto.models import Challan, Rules, Vehicle 
from django.contrib import messages
# from django.core.mail import EmailMessage
# from django.core.mail import EmailMultiAlternatives
# from django.conf import settings
from django.template.loader import render_to_string
import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'home.html')


def askquestions(request):
    return render(request,'askquestions.html')

def myanswers(request):
    return render(request,'myanswers.html')

def index2(request):
    return render(request,'home2.html')


def askquestions2(request):
    return render(request,'askquestions2.html')

def myanswers2(request):
    return render(request,'myanswers2.html')

def reviewmanager(request):
    return render(request,'reviewmanager.html')


def reviewemployee(request):
    return render(request,'reviewemployee.html')

def index3(request):
    return render(request,'home3.html')

def askquestions3(request):
    return render(request,'askquestions3.html')

def myanswers3(request):
    return render(request,'myanswers3.html')

def sharethoughts(request):
    return render(request,'sharethoughts.html')

def solveissues(request):
    return render(request,'solveissues.html')

#To add questions to database

def addq(request):
    if request.method == "POST":
        qtitle=request.POST.get('title')
        qdesc=request.POST.get('description')
        qatt=request.POST.get('attachment')
        print(qtitle)
        print(qdesc)
        sug_data= Suggestion_Data(Title=qtitle, Mail="a@gmail.com", Description=qdesc, Attachment=qatt, Entry_Time=datetime.now().date())
        sug_data.save()
        return redirect('../')
    
    else:
        pass

def showmyquestions(request):
    myquestions = list(Suggestion_Data.objects.all().values().reverse())

    context1={
        'q' : myquestions
    }

    return render(request,'myanswers.html',context1)