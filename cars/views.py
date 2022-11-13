from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from . serializers import CarSerilalizer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerilalizer(cars, many = True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CarSerilalizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerilalizer(car)
        return Response(serializer.data)

    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    
    
    

