from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):

    if request.method == 'POST':
        form = forms.studentFrom(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form = forms.studentFrom()
        
    return render(request,'home.html',{'form':form})