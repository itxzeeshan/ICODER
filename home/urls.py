from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('contact', views.contact, name='home'),
    path('about', views.about, name='blog'),
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
