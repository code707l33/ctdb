from django.urls import path

from .views import comment_create, comment_delete,comment_list, comment_update,comment_message_list

app_name = 'comment'

urlpatterns = [
    path('comments/', comment_list, name='comment_list'),
    path('comments/add/', comment_create, name='comment_create'),
    path('comments/<int:pk>/change/', comment_update, name='comment_update'),
    path('comments/<int:pk>/delete/', comment_delete, name='comment_delete'),
    path('comments/<int:pk>/comment_message/', comment_message_list, name='comment_message_list'),

]
