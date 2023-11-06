from django.urls import path, include
from app_users import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact')
]