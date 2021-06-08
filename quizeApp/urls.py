
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
 ]
