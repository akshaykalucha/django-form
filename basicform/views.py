from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    return render(request, 'basicform/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("TExt: " + form.cleaned_data['text'])



    return render(request, 'basicform/form.html', {'form':form})