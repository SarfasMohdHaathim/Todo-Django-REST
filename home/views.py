from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.
@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        data=Todo.objects.all()
        serializer=TodoSerializer(data ,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data=Todo.objects.create(
            title=request.data['title'],
            des=request.data['des']
        )
        serializer=TodoSerializer(data ,many=True)
        return Response(serializer.data)

@api_view(['GET',"PUT","DELETE"])
def todo(request,id):
    data=Todo.objects.get(id=id)
    print(data,"0000000000000")
    if request.method == 'GET':
        serializer=TodoSerializer(data ,many=False)
        return Response(serializer.data) 
    if request.method == 'PUT':
        data.title=request.data['title']
        data.des=request.data['des']
        data.save()
        serializer=TodoSerializer(data ,many=False)
        return Response(serializer.data) 
    if request.method == 'DELETE':
        data.delete()
        serializer=TodoSerializer(data ,many=False)
        return redirect('home')
