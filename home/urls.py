from django.urls import path
from home import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('dashboard/home/HomeSlider/', views.homeslider, name='dashboard/home/HomeSlider/'),
]
