from django.shortcuts import render

from myapp.models import Student


def home(request):
    student=Student.objects.all()
    return render(request,'home.html',context={'student':student})
def about(request):
    return render(request,'about.html')