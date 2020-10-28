from django.shortcuts import render, redirect
from medclapp.forms import UserAdminCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, 'medclapp/register.html', {'form': form})



def loginpage(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        print(email,",",password)
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return render(request, 'medclapp/success.html')
        else:
            return redirect("login")
    return render(request,"medclapp/userlogin.html")

def logOut(request):
    logout(request)
    return redirect("login")

