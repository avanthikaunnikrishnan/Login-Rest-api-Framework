import queue
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.views import APIView

from .models import SimpleUser
from .serializers import SimpleUserSerializer
from rest_framework.response import Response

# Create your views here.
class UserViewSet(APIView):
    def get(self,request, format=None):
        # returns a list of users
        users = SimpleUser.objects.all()
        serializer = SimpleUserSerializer(users, many=True)
        return Response({'data': 'login'})

    def post(self, request, format=None):
        print(request.data)
        username = request.data[0]['username']
        password = request.data[0]['password']

        try:
            object = SimpleUser.objects.get(queue(username=username) & queue (password=password))
            print(f"object is {object}------------")

            serializer = SimpleUserSerializer(object)
            return Response({'status': 'success'})

        except SimpleUser.DoesNotExist:
            return Response({'status': 'unsuccessfull'})