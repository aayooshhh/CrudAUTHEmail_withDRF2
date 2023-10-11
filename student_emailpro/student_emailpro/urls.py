"""
URL configuration for student_emailpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from student_app.views import StudentViewset
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

router=DefaultRouter()
router.register('students',StudentViewset,basename='students')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include(router.urls)),
    path('',include('auth_app.urls')),
    path('v1/access/',token_obtain_pair),
    path('v1/refresh/',token_refresh)
]