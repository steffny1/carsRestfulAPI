#from django.conf.urls import url
from django.urls import re_path
from cars import views

urlpatterns = [
    re_path(r'^car-categories/$', views.CarCategoryList.as_view(),
        name=views.CarCategoryList.name),
    re_path(r'^car-categories/(?P<pk>[0-9]+)$',
        views.CarCategoryDetail.as_view(), name=views.CarCategoryDetail.name),
    re_path(r'^cars/$', views.CarList.as_view(), name=views.CarList.name),
    re_path(r'^cars/(?P<pk>[0-9]+)$',
        views.CarDetail.as_view(), name=views.CarDetail.name),
    re_path(r'^drivers/$', views.DriverList.as_view(), name=views.DriverList.name),
    re_path(r'^drivers/(?P<pk>[0-9]+)$',
        views.DriverDetail.as_view(), name=views.DriverDetail.name),
    re_path(r'^competitions/$', views.CompetitionList.as_view(),
        name=views.CompetitionList.name),
    re_path(r'^compeitions/(?P<pk>[0-9]+)$', views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name),
    re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
