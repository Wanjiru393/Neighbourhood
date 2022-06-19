from django.urls import re_path as url
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)