from rest_framework import serializers
from .models import User, U_tracking_return, Awb

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name')

class AwbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Awb
        fields = ('id', 'url', 'awb_no', 'user', 'awbs_list')

class U_tracking_returnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = U_tracking_return
        fields = ('id',
                  'url',
                  'ori',
                  'des',
                  'eta',
                  'etd',
                  'flight_no',
                  'status')