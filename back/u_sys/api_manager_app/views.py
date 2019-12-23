from django.shortcuts import render
from rest_framework import viewsets
from .models import U_tracking_return, User, Awb
from . serializers import UserSerializer, U_tracking_returnSerializer, AwbSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AwbView(viewsets.ModelViewSet):
    queryset = Awb.objects.all()
    serializer_class = AwbSerializer

class U_tracking_returnView(viewsets.ModelViewSet):
    queryset = U_tracking_return.objects.all()
    serializer_class = U_tracking_returnSerializer