from django.urls import path
from . import views

app_name = 'timeline'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_1/', views.index_1, name='index_1'),
    path('create/', views.create, name='create'),
    path('create_1/', views.create_1, name='create_1'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('delete_1/<int:pk>/', views.delete_1, name='delete'),
    path('like/', views.like, name='like'),
    path('like_1/', views.like_1, name='like_1'),
]