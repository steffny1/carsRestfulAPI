from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from cars.models import CarCategory, Car, Driver, Competition
from cars.serializers import CarCategorySerializer, CarSerializer, DriverCompetitionSerializer, DriverSerializer, CompetitionSerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from cars import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle

# Create your views here.

# use the Browsable API to view or navigate through the API with resources and relationships
# filtering against query parameters


class CarCategoryList(generics.ListCreateAPIView):
    # below attributes are inherited from the generics.ListCreateAPIView class
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer
    name = 'carcategory-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class CarCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer
    name = 'carcategory-detail'


class CarList(generics.ListCreateAPIView):
    #use the settings specified for the 'cars' scope and the
    # ScopeRateThrottle class for throttling
    throttle_scope = 'cars'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-list'
    filter_fields = ('name', 'car_category',
                     'manufacturing_date', 'has_it_competed',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'manufacturing_date')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          custompermission.IsCurrentUserOwnerOrReadOnly,)
    
    #make the authenticated user that makes the request the owner of the new car
    #override the perform_create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    #use the settings specified for the 'cars' scope and the
    # ScopeRateThrottle class for throttling
    throttle_scope = 'cars'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          custompermission.IsCurrentUserOwnerOrReadOnly,)


class DriverList(generics.ListCreateAPIView):
    #use the settings specified for the 'drivers' scope and the
    # ScopeRateThrottle class for throttling
    throttle_scope = 'drivers'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-list'
    filter_fields = ('name', 'gender',
                     'races_count',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'races_count')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    #use the settings specified for the 'drivers' scope and the
    # ScopeRateThrottle class for throttling
    throttle_scope = 'drivers'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-detail'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

# custom filter to filter the competition values in the Competition Model fields
# It uses attributes from the django-filter module to filter the data based on the
# user's search query


class CompetitionFilter(FilterSet):
    from_achievement_date = DateTimeFilter(
        name='speed_achievement_date', lookup_expr='gte')
    # This attribute is a django_filters.DateTimeFilter
    # instance that allows the request to filter the competitions whose
    # achievement_date DateTime value is less than or equal to the specified DateTime value.
    to_achievement_date = DateTimeFilter(
        name='speed_achievement_date', lookup_expr='lte')
    # gte means greater than or equal to
    min_distance_in_km = NumberFilter(name='speed_in_km', lookup_expr='gte')
    # lte means less than or equal to
    max_distance_in_km = NumberFilter(name='speed_in_km', lookup_expr='lte')
    car_name = AllValuesFilter(name='car.name')
    driver_name = AllValuesFilter(name='driver.name')

    class Meta:
        model = Competition
        fields = ('speed_in_km',
                  'from_achievement_date',
                  'to_achievement_date',
                  'min_distance_in_km',
                  'max_distance_in_km',
                  # car__name will be accessed as car_name
                  'car_name',
                  # driver__name will be accessed as driver_name
                  'driver_name',)


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = DriverCompetitionSerializer
    name = 'competition-list'
    filter_class = CompetitionFilter
    ordering_fields = ('speed_in_km', 'speed_achievement_date',)


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = DriverCompetitionSerializer
    name = 'competition-detail'
    
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'car_categories': reverse(CarCategoryList.name, request=request), 'cars': reverse(CarList.name, request=request), 'drivers': reverse(DriverList.name, request=request), 'competitions': reverse(CompetitionList.name, request=request)})
