from django.urls import path
from . import views
urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('click',views.click,name='click'),
    path('form', views.form, name='form'),
    path('confirm', views.confirm, name='confirm'),


]
