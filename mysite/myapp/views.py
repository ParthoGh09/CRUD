from django.shortcuts import render, redirect

from myapp.forms import StudentForm


# Create your views here.

def create_form(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if method.is_valid:
            request.save()
            return redirect('/')
    else:
        form=StudentForm

    return render(request,'forms.html',context={'form':form})