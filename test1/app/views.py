from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    current_datetime = datetime.now()
    print(current_datetime)
    return render(request, 'home.html')