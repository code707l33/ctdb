from django.urls import path

from .views import archive_create, archive_delete, archive_list, archive_update
# from .views import journals_list, journals_create, journals_update, journals_delete

app_name = 'archive'

urlpatterns = [
    path('archives/', archive_list, name='archive_list'),
    path('archives/add/', archive_create, name='archive_create'),
    path('archives/<int:pk>/change/', archive_update, name='archive_update'),
    path('archives/<int:pk>/delete/', archive_delete, name='archive_delete'),
    # path('archives/', journals_list, name='journals_list'),
    # path('archives/add/', journals_create, name='journals_create'),
    # path('archives/<int:pk>/change/', journals_update, name='journals_update'),
    # path('archives/<int:pk>/delete/', journals_delete, name='journals_delete'),
]
