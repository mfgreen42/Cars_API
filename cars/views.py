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
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

