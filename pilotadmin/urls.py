from django.urls import path

from .views import pilotadmin_list, pilotadmin_content, pilotadmin_create, pilotadmin_update, pilotadmin_delete


app_name = 'pilotadmin'

urlpatterns = [
    path('pilotadmin/', pilotadmin_list, name='pilotadmin_list'),
    path('pilotadmin/<int:pk>/', pilotadmin_content, name='pilotadmin_content'),
    path('pilotadmin/add/', pilotadmin_create, name='pilotadmin_create'),
    path('pilotadmin/<int:pk>/change/', pilotadmin_update, name='pilotadmin_update'),
    path('pilotadmin/<int:pk>/delete/', pilotadmin_delete, name='pilotadmin_delete'),
]
