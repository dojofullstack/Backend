from .models import *
from rest_framework import serializers




class ArticuloBlogSerial(serializers.ModelSerializer):

    class Meta:
        model = ArticuloBlog
        fields = '__all__'


