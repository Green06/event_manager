from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("home")
def home(request):
    return render(request, 'events/index.html')