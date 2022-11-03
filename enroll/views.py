from django.shortcuts import render, HttpResponseRedirect
from .forms import EditUserAdminForm, SignUpFrom, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


def SignUp(request):

    if request.method == "POST":
        fm = SignUpFrom(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created Successfully!!')
    else:
        fm = SignUpFrom()
    return render(request, 'enroll/RegistrationForm.html', {'form':fm})


def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('profile')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/UserLogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('profile')



def UserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                user = User.objects.all()
                fm = EditUserAdminForm(request.POST, instance= request.user)
                if fm.is_valid():
                    messages.success(request, 'Profile is Updated!!')
                    fm.save()
            else:
                user = None
                fm = EditUserProfileForm(request.POST, instance= request.user)
                if fm.is_valid():
                    messages.success(request, 'Profile is Updated!!')
                    fm.save()
        else:
            if request.user.is_superuser == True:
                user = User.objects.all()
                fm = EditUserAdminForm(instance=request.user)
            else:
                user = None
                fm = EditUserProfileForm(instance = request.user)
        return render(request, 'enroll/profile.html', {'name': request.user, 'form':fm, 'Users': user})
    else:
        return HttpResponseRedirect('login')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('login')

def ChanagePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('profile')
        else:
            fm = SetPasswordForm(user =  request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('login')

