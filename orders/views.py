from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
# @login_required
def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "login.html", {"message": "Login Successful!"})
        else:
            return render(request, "login.html", {"message": "Invalid Credentials"})
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        
        if not password == confirmation:
            return render(request, "signup.html", {"message": "Passwords do not match"})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return render(request, "login.html", {"message": "Sucessfully signed up. Please login"})
    else:
        return render(request, "signup.html")