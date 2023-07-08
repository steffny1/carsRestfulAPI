from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from cars import views

class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'mv-categories': reverse(views.CarCategoryList.name, request=request),
            'mv': reverse(views.CarList.name, request=request),
            'drivers': reverse(views.DriverList.name, request=request),
            'competitions': reverse(views.CompetitionList.name, request=request)
})