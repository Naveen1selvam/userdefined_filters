from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'data':'HoW ArE YYYYooouuuu'}
    return render(request,'filter.html',d)