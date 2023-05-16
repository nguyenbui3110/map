from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('location', views.location_view, name='location'),
    path('', views.login_account, name='login_account'),
    path('logout', views.logout_account, name='logout_account'),
    path('camera', views.camera, name='camera'),
    path('get_image/', views.get_image, name='get_image'),
]
