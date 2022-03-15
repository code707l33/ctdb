from django.urls import path

from .views import comment_create, comment_delete,comment_list, comment_update
from .views import comment_message_list, comment_message_create

app_name = 'comment'

urlpatterns = [
    path('comments/', comment_list, name='comment_list'),
    path('comments/add/', comment_create, name='comment_create'),
    path('comments/<int:pk>/change/', comment_update, name='comment_update'),
    path('comments/<int:pk>/delete/', comment_delete, name='comment_delete'),
    
    path('comments/<int:pk>/messages/', comment_message_list, name='comment_message_list'),
    path('comments/<int:pk>/messages/add/', comment_message_create, name='comment_message_create'),

]
