from django.shortcuts import render
from datetime import datetime

def dashboard(request):
    return render(request, "home/home.html", {"year": datetime.now().year})