from django.shortcuts import render

# Create your views here.
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect

def signup(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
