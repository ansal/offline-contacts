from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Utility function that logins an user
def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    request.session.set_expiry(0)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            request.session.set_expiry(0)
            auth_login(request, user)
            return HttpResponseRedirect(
                reverse('dashboard')
            )
        else:
            return HttpResponseRedirect(
                reverse('accounts_login') + '?disabled=true'
            )
    else:
        return HttpResponseRedirect(
            reverse('accounts_login') + '?error=True'
        )

# User registration view
def register(request):

    response = {}
    response.update(csrf(request))

    if request.method == 'GET':
        return render(request, 'register.html', response)

    form_error = False

    if 'name' in request.POST and request.POST['name']:
        name = request.POST['name']
        response['name'] = name
    else:
        form_error = True
    
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        response['username'] = username
    else:
        form_error = True

    if 'password' in request.POST and request.POST['password']:
        password = request.POST['password']
    else:
        form_error = True

    if form_error:
        response['form_error'] = True
        return render(request, 'register.html', response)

    # Check whether the username is taken or not!
    try:
        user = User.objects.get(username=username)
    except:
        user = User(
            first_name = name,
            username = username,
        )
        user.set_password(password)
        user.save()
        return authenticate_user(request)
    else:
        response['username_exists'] = True
        return render(request, 'register.html', response)

# User login view
def login(request):

    response = {}
    response.update(csrf(request))

    if request.method == 'GET':

        if 'error' in request.GET and request.GET['error']:
            response['login_error'] = True

        return render(request, 'login.html', response)

    if request.method == 'POST':
        return authenticate_user(request)

# User logout view
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(
        reverse('accounts_login')
    )