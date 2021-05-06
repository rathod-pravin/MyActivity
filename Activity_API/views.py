from django.shortcuts import HttpResponse
from rest_framework.response import Response
from .serializers import MyTaskSerializer
from .models import MyTask
from rest_framework.decorators import api_view


def Index(request):
    return HttpResponse('<h1>this is test page...</h1>')


@api_view(['GET'])
def MyAPI(request):
    api_urls = {
        'List': '/task-list/',
        'Detail': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def MyTaskList(request):
    tasks = MyTask.objects.all()
    serializer = MyTaskSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def MyTaskDetail(request, pk):
    tasks = MyTask.objects.get(id=pk)
    serializer = MyTaskSerializer(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def MyTaskUpdate(request, pk):
    task = MyTask.objects.get(id = pk)
    serializer = MyTaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def MyTaskCreate(request):
    serializer = MyTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def MyTaskDelete(request, pk):
    task = MyTask.objects.get(id = pk)
    task.delete()
    return Response("Activity deleted successfully.")