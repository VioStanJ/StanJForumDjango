from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django import forms
from connexion.models import User

# Create your views here.
def home(request):
    return render(request,'connexion.html')

def sign(request):
    return render(request,'register.html')

def goSign(request):
    return redirect('register')

def getUserToSave(request):
    if request.method == "POST":
        if request.POST.get('last').strip():
            if request.POST.get('first').strip():
                if request.POST.get('mail').strip():
                    if request.POST.get('password').strip() and request.POST.get('password2').strip():
                        if request.POST.get('password') == request.POST.get('password2'):
                            if request.POST.get('check'):
                                usr = User()
                                usr.firstname = request.POST.get('first')
                                usr.lastname = request.POST.get('last')
                                usr.mail = request.POST.get('mail')
                                usr.fonction = request.POST.get('fonc')
                                usr.pass1 = request.POST.get('password')
                                usr.pass2 = request.POST.get('password2')
                                usr.save()
                                return HttpResponse('<h1>Welcome to The Fo<strong>Rhum</strong> !</h1><br><a href="connect">Connect</a>')
                            else:
                                return HttpResponse('<h1>Accept Conditions to Sign Up !</h1>')
                        else:
                            return HttpResponse('<h1>Password is not same !</h1>')
                    else:
                        return HttpResponse('<h1>Please insert your password and verify !</h1>')
                else:
                    return HttpResponse('<h1>Please insert a valid Email !</h1>')
            else:
                return HttpResponse('<h1>Please insert your Firstname !</h1>')
        else:
            return HttpResponse('<h1>Please insert your Lastname !</h1>')
        