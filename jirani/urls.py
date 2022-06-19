from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('notifications',views.notification, name='notifications'),
    path('health',views.health, name='health'),
    path('authorities',views.authorities, name='authorities'),
    path('businesses',views.businesses, name='businesses'),
    path('my-profile/',views.my_profile, name='my-profile'),
    path('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
]

