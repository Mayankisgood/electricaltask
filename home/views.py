from xml.etree.ElementTree import Comment
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# An HTTP response class with a string as content.This content can be read, appended to, or replaced


def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2": "Rohan is great"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        comment = request.POST.get('comment')
        contact = Contact(name=name, phonenumber =phonenumber,comment= comment, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')





    