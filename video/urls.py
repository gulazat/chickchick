from django.urls import path,re_path

from . import views

app_name = 'video'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:pk>/', views.video_detail, name='detail'),
    path('category/<int:pk>/', views.category, name='video_category'),
    path('tags/<int:pk>/', views.tag, name='video_tag'),
    path('all/', views.all, name='all_video'),
    path('all_tags/', views.all_tag, name='all_tags'),
    path('introduc/', views.introduction, name='introduction'),

]