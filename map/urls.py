from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('location', views.location_view, name='location'),
    path('', views.login_account, name='login_account'),
    path('logout', views.logout_account, name='logout_account'),
    path('camera', views.camera, name='camera'),
    path('get_image/', views.get_image, name='get_image'),
    path('table', views.table, name='table'),
    path('update-status/', views.update_status, name='update_status'),
    path('update-mode/', views.update_mode, name='mode'),
    path('fetch-data/', views.fetch_data, name='fetch_data'),
]
