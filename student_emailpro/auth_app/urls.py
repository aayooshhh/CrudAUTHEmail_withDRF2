from django.urls import path
from .views import UserApi,logoutf

urlpatterns=[
    path('user/',UserApi.as_view()),
    path('logout/',logoutf)

]