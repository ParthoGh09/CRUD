from django import forms

from myapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','s_id','dob','email','department']