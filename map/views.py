from django.shortcuts import render
from django.http import JsonResponse
from . import models
from DeviveManager import settings
import firebase
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
import json

config = {
    "apiKey": "AIzaSyCtSA5ZdMkAx0sU80U9XFit1RwELYkZSqo",
    "authDomain": "smartlight-384608.firebaseapp.com",
    "databaseURL": "https://smartlight-384608-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "smartlight-384608",
    "storageBucket": "smartlight-384608.appspot.com",
    "messagingSenderId": "966374978915",
    "appId": "1:966374978915:web:3dfd66163106082519cf56",
}

# here we are doing firebase authentication
app = firebase.initialize_app(config)
authe = app.auth()
database = app.database()


# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_account')
    gps = dict(database.child("gps").get().val())
    print(gps)
    context = {
        'location': gps,
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'username': request.user.username
    }
    return render(request, 'map/index.html', context)


def location_view(request):
    # Here you would query the database or fetch data from an external API to get the latest location data
    location = dict(database.child("gps").get().val())
    print(location)
    return JsonResponse(location)


def login_account(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def logout_account(request):
    if not request.user.is_authenticated:
        return redirect('login_account')
    else:
        logout(request)
        return redirect('login_account')

def camera(request):
    if not request.user.is_authenticated:
        return redirect('login_account')
    return render(request, 'map/camera.html')

def get_image(request):
    image_base64 = database.child("image").get().val()
    # Return the base64 string as a JSON response
    return JsonResponse({'image_base64': image_base64})

def table(request):
    if not request.user.is_authenticated:
        return redirect('login_account')
    devices= dict(database.child("gps").get().val())
    auto= database.child("auto").get().val()
    if auto == 1:
        auto = "auto"
    else:
        auto = "manual"
    context={
        'devices':devices,
        'mode':auto,
    }
    print(devices)
    return render(request, 'map/deviceTable.html',context)

def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        device_key = data.get('deviceKey')
        new_status = data.get('newStatus')
        database.child("gps").child(device_key).update({"status": new_status})
        print(device_key)
        print(new_status)
        # Return a JSON response to indicate success
        response = {'status': 'success'}
        return JsonResponse(response)
    
def update_mode(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_mode = data.get('newMode')
        if new_mode == "auto":
            new_mode = 1
        else:
            new_mode = 0
        database.child("auto").set(new_mode)
        print(new_mode)
        # Return a JSON response to indicate success
        response = {'status': 'success'}
        return JsonResponse(response)
    
def fetch_data(request):
    # Retrieve the updated data from the database or any other source
    devices= dict(database.child("gps").get().val())
    auto= database.child("auto").get().val()
    if auto == 1:
        auto = "auto"
    else:
        auto = "manual"

    # Prepare the response data
    data = {
        'devices': devices,
        'mode': auto,
    }

    return JsonResponse(data)
