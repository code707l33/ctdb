from django.urls import path

from .views import pilotadmin_list


app_name = 'pilotadmin'

urlpatterns = [
    path('pilotadmin/', pilotadmin_list, name='pilotadmin_list'),
]
