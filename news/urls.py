from django.urls import path

from .views import news_create, news_delete, news_list, news_update, dep_news_list

app_name = 'news'

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('dep-news/', dep_news_list, name='dep_news_list'),
    path('news/add/', news_create, name='news_create'),
    path('news/<int:pk>/change/', news_update, name='news_update'),
    path('news/<int:pk>/delete/', news_delete, name='news_delete'),
]
