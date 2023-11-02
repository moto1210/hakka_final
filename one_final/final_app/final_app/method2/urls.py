from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('toppage/', views.toppage, name="toppage"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('toppage/sub2.htm/',views.sub2_view,name="sub2"),
    path('toppage/sub3.htm/',views.sub3_view, name='sub3'),
    path('tooppage/sub2.htm/sub4.htm/', views.sub4_view, name='sub4'),
]