from django.shortcuts import render
from django.http import JsonResponse
from . import models
from DeviveManager import settings
import firebase
config={
    "apiKey": "AIzaSyCtSA5ZdMkAx0sU80U9XFit1RwELYkZSqo",
    "authDomain": "smartlight-384608.firebaseapp.com",
    "databaseURL": "https://smartlight-384608-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "smartlight-384608",
    "storageBucket": "smartlight-384608.appspot.com",
    "messagingSenderId": "966374978915",
    "appId": "1:966374978915:web:3dfd66163106082519cf56",
}

#here we are doing firebase authentication
app=firebase.initialize_app(config)
authe = app.auth()
database=app.database()


# Create your views here.
def index(request):
    gps=dict(database.child("gps").get().val())
    print(gps)
    context={
        'location':gps,
        'api_key':settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'map/index.html', context)
def location_view(request):
    # Here you would query the database or fetch data from an external API to get the latest location data
    location=dict(database.child("gps").get().val())
    print(location)
    return JsonResponse(location)
