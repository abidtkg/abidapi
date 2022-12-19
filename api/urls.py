from django.urls import path
from . import views

urlpatterns = [
    path('/get/', views.getData),
    path('/set/', views.setData)
]
