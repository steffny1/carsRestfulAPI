#from django.re_paths import re_path
from django.urls import re_path
from cars import views
from cars.v2 import views as views_v2

urlpatterns = [
re_path(r'^mv-categories/$', views.CarCategoryList.as_view(),name=views.CarCategoryList.name),
re_path(r'^mv-categories/(?P<pk>[0-9]+)$',views.CarCategoryDetail.as_view(),name=views.CarCategoryDetail.name),
re_path(r'^mv/$', views.CarList.as_view(),name=views.CarList.name),
re_path(r'^mv/(?P<pk>[0-9]+)$',views.CarDetail.as_view(),name=views.CarDetail.name),
re_path(r'^drivers/$',views.DriverList.as_view(),name=views.DriverList.name),
re_path(r'^drivers/(?P<pk>[0-9]+)$',views.DriverDetail.as_view(),name=views.DriverDetail.name),
re_path(r'^competitions/$',views.CompetitionList.as_view(),name=views.CompetitionList.name),
re_path(r'^competitions/(?P<pk>[0-9]+)$',views.CompetitionDetail.as_view(),name=views.CompetitionDetail.name),
re_path(r'^$',views_v2.ApiRootVersion2.as_view(),name=views_v2.ApiRootVersion2.name),
]