import json

from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

# Utility function to raise 400 error
def json_validation_error(name):
    return JsonResponse({
        'error': name + ' is required'
    }, status=400)

# Utility function to raise 404 error
def json_404_error():
    return JsonResponse({
        'error': 'object not found'
    }, status=404)

# Utility function that returns a contact as a JSON object
def contact_as_json(contact):
    return JsonResponse({
        'id': contact.pk,
        'name': contact.name,
        'email': contact.email,
        'phone': contact.phone
    })

@login_required
def dashboard(request):

    response = {}
    response.update( csrf(request) )

    response['user'] = request.user

    return render(request, 'dashboard.html', response)

# For GET, Lists out all contacts created by user.
# For POST, creates new contact
@login_required
@csrf_exempt
def contact(request):

    if request.method == 'GET':
        contacts = Contact.objects.filter(
            user = request.user
        ).order_by('name')
        response = []
        for contact in contacts:
            response.append({
                'id': contact.pk,
                'name': contact.name,
                'phone': contact.phone,
                'email': contact.email
            })
        return JsonResponse( response, safe=False )

    if request.method == 'POST':
        contact = Contact(user = request.user)

        request_json = json.loads( request.body )

        if 'name' in request_json and request_json['name']:
            contact.name = request_json['name']
        else:
            return json_validation_error('name')

        if 'email' in request_json and request_json['email']:
            contact.email = request_json['email']
        else:
            return json_validation_error('email')

        if 'phone' in request_json and request_json['phone']:
            contact.phone = request_json['phone']
        else:
            return json_validation_error('phone')

        contact.save()

        return contact_as_json(contact)

# For PUT, updates the object
# For DELETE, deletes the object
@login_required
@csrf_exempt
def contact_update(request, pk=None):

    try:
        contact = Contact.objects.get(user = request.user, pk=pk)
    except:
        return json_404_error()

    if request.method == 'PUT':

        request_json = json.loads( request.body )

        if 'name' in request_json and request_json['name']:
            contact.name = request_json['name']
        else:
            return json_validation_error('name')

        if 'email' in request_json and request_json['email']:
            contact.email = request_json['email']
        else:
            return json_validation_error('email')

        if 'phone' in request_json and request_json['phone']:
            contact.phone = request_json['phone']
        else:
            return json_validation_error('phone')

        contact.save()

        return contact_as_json(contact)

    if request.method == 'DELETE':
        contact.delete()
        return JsonResponse({
            'success': 'object deleted'
        })