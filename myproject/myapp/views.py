from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cal(request):
    val1=int(request.POST['Height'])
    val2=int(request.POST['Weight'])
    res = val2/val1*val1

    return render(request,'result.html',{'result':res})