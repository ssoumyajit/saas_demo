from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountCreate.as_view(), name=views.AccountCreate.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<uuid:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('myhood', views.MyHoodDetail.as_view(), name=views.MyHoodDetail.name),
]
