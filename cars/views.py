from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from . serializers import CarSerilalizer
# Create your views here.

@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()

    serializer = CarSerilalizer(cars, many = True)

    

    return Response(serializer.data)
