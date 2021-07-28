from django.urls import path

from .views import archive_create, archive_delete, archive_list, archive_update
from .views import journals_list, journals_create

app_name = 'archive'

urlpatterns = [
    path('archives/', archive_list, name='archive_list'),
    path('archives/add/', archive_create, name='archive_create'),
    path('archives/<int:pk>/change/', archive_update, name='archive_update'),
    path('archives/<int:pk>/delete/', archive_delete, name='archive_delete'),
    path('archives/journals/', journals_list, name='journals_list'),
    path('archives/journals/add/', journals_create, name='journals_create'),
]
