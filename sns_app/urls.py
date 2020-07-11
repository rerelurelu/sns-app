from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('login/', views.loginfnc, name='login'),
    path('list/', views.listfnc, name='list'),
    path('logout/', views.logoutfnc, name='logout'),
    path('detail/<int:pk>/', views.detailfnc, name='detail'),
    path('good/<int:pk>/', views.goodfnc, name='good'),
    path('read/<int:pk>/', views.readfnc, name='read'),
    path('create/', views.SnsCreate.as_view(), name='create'),
]

