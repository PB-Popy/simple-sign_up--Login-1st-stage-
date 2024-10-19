from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signupPage (request):
    
    if request.method=='POST':
        
        profile_pic=request.FILES.get('profile_pic')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        usertype=request.POST.get('usertype')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        contact_no=request.POST.get('contact_no')

        if password==confirm_password:

            user=CustomUser.objects.create_user(
                profile_pic=profile_pic,
                username=username,
                email=email,
                password=password,
                usertype=usertype,
                gender=gender,
                age=age,
                contact_no=contact_no,
               
            )

            if usertype=='viewer':
                viewersProfileModel.objects.create(user=user)

            elif usertype=='blogger':
                BloggerProfileModel.objects.create(user=user)

            return redirect('signInPage')
    
    return render (request,'signupPage.html')

def signInPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except CustomUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

def logoutPage(request):
    
    logout(request)

    return redirect('signInPage')

@login_required
def homePage(request):
    return render(request, 'homePage.html')

@login_required
def ProfilePage(request):
    return render(request, 'ProfilePage.html')