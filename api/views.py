from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Property
from api.serializer import PropertySerialiazer 

# Create your views here.
@api_view(['GET'])
def property_list(request):
    properties = Property.objects.all() #complex data

    serializer = PropertySerialiazer(properties, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_property(request):
    # properties = Property.objects.all() #complex data

    serializer = PropertySerialiazer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['PUT','GET', 'DELETE'])
def update_property(request,pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = PropertySerialiazer(property)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PropertySerialiazer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        property.delete
        return "Property deleted successfull"
        


    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     return Response(serializer.errors)
