from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
     path('register/', views.register, name='register'),
    path('update/<int:pk>/', views.update, name='update'),
    path('read/<int:pk>/', views.read, name='read'),
    path('features/', views.features, name = 'features'),
    path('chart/', views.chart, name='chart'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
