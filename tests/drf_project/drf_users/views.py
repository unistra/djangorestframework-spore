from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from . import serializers

# Create your views here.

class ListCreateUsers(generics.ListCreateAPIView):

    is_spore_view = True
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    renderer_classes = (JSONRenderer, )



class ListCreateSuperUsers(generics.ListCreateAPIView):

    is_spore_view = True
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = serializers.UserSerializer
    renderer_classes = (JSONRenderer, )
