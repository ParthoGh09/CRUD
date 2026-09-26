from django.shortcuts import render, redirect

from myapp.forms import StudentForm

from django.shortcuts import render

from myapp.forms import StudentForm

# Create your views here.

def create_form(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=StudentForm

    return render(request,'forms.html',context={'form':form})