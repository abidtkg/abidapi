from django.urls import path
from . import views

urlpatterns = [
    path('/get/', views.getData),
    path('/set/', views.setData),
    path('/user/users', views.getUsers),
    path('/user/create', views.createUser)
]
