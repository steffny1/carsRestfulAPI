"""
URL configuration for carsRestfulAPI project.

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
from django.urls import path, re_path, include
# from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #unit testing not working on versioning urls
    #re_path(r'^v1/api-auth/', include(('rest_framework.urls','rest_framework v1',), namespace='rest_framework v1')),
    #re_path(r'^v1/', include(('cars.urls','v1'), namespace='v1')),
    #re_path(r'^v2/api-auth/', include(('rest_framework.urls','rest_framework v2'), namespace='rest_framework v2')),
    #re_path(r'^v2/', include(('cars.v2.urls','v2',), namespace='v2')),
    re_path(r'^', include('cars.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls'))
]
