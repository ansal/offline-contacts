import json

from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Contact

def dashboard(request):

    response = {}
    response.update( csrf(request) )

    return render(request, 'dashboard.html', response)