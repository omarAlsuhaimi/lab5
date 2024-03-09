from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.
people = []
def index(request):
    if request.method == "POST":
        form = newPersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            newPerson = person(name,password)
            people.append(newPerson)

            return HttpResponseRedirect(reverse("display"))



    return render(request,'add.html',{"form":newPersonForm()})

def display(request):
    return render(request,"display.html",{"people":people})


class newPersonForm(forms.Form):
    name = forms.CharField(label = "username")
    password = forms.CharField(label = "password")
class person():
    def __init__(self,n,p):
        self.name = n
        self.password = p