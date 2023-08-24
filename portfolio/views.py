from django.shortcuts import render
from .models import *
from .forms import MessageForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')

    home = Home.objects.first()
    skills = Skill.objects.all()
    timelines = TimeLine.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Project.objects.all()
    contact = Contact.objects.first()
    accounts = SocialMedia.objects.all()
    form  = MessageForm()

    return render(request, 'index.html',locals())    