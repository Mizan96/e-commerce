from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.contrib.auth import update_session_auth_hash
import random
from products_app.models import ProductCategory
from accounts_app.signals import create_shipping_profile
from billing_app.signals import create_billing_info
from django.core.mail import send_mail
from accounts_app.verfication import email_creation
from products_app.models import ProductCategory

from accounts_app.forms import ( 
    LoginForm, 
    RegisterForm,
    VerificationForm
    )


def login_view(request):
    cat = ProductCategory.objects.all()
    form = LoginForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    obj = ProductCategory.objects.all()
    context ={
        'form': form,
        'objects': obj,
        'cat': cat
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
    return render(request, 'accounts/login.html', context)

def register_view(request):
    cat = ProductCategory.objects.all()
    form = RegisterForm(request.POST or None)
    obj = ProductCategory.objects.all()
    context = {
        'form':form,
        'objects': obj,
        'cat': cat
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        instance =  User.objects.create_user(
                                username = username, 
                                email = email, 
                                password = password,
                                first_name = first_name,
                                last_name = last_name,
                                is_active = False,
                                is_staff = False,
                                is_superuser = False
                                )
        request.session['code'] = random.randint(111111,999999)
        message = email_creation(instance.first_name+' '+instance.last_name, request.session['code'])
        send_mail(
        'Activation code',
        message,
        'microcir13@gmail.com',
        [instance.email],
        fail_silently=False,
            )
        create_shipping_profile.send(sender=instance.__class__, instance=instance)
        create_billing_info.send(sender=instance.__class__, instance=instance)
        return redirect('accounts:email_verfication', username=username)
    return render(request, 'accounts/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('home') 

def verification_view(request, username):
    cat = ProductCategory.objects.all()
    context = {
        'cat': cat
    }
    if request.method == 'POST':
        code = int(request.POST.get('verification-code'))
        if code ==  int(request.session['code']):
            instance = User.objects.get(username=username)
            instance.is_active = True
            instance.save()
            return redirect('accounts:email_successful')
    return render(request, 'accounts/verification.html', context)

def successful_view(request):
    cat = ProductCategory.objects.all()
    context = {
        'cat': cat
    }
    return render(request, 'accounts/successful.html', context)