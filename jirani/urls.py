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
    path('user/',views.user_profile,name='user-profile'),
    path('new/business',views.new_business, name='new-business'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('new/notification',views.new_notification, name='new-notification'),
    path('update/profile',views.update_profile, name='update-profile'),
]

# (?P<username>\w{0,50})
