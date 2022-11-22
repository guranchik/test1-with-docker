from django.shortcuts import render
import datetime
from .models import Date
# Create your views here.
def home(request):
    time=str(int(datetime.datetime.now().hour+3))+":"+str(datetime.datetime.now().minute)
    Date1 = Date()
    Date1.date = time
    Date1.save()
    dates=""
    for a in Date.objects.all():
        dates= dates+" "+a.date
    return render(request, 'home.html',{"dates": dates})