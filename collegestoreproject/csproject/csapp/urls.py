from .import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('form/',views.form,name='form'),
    path('message/',views.message,name='message'),
    path('logout/',views.logout,name='logout')


]
