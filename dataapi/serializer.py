from dataclasses import field
from rest_framework import serializers
from .models import DateBhav, Securities, Bhav

class BhavSeri(serializers.ModelSerializer):
    class Meta:
        model = Bhav
        fields = '__all__'


class Datebhavseri(serializers.ModelSerializer):
    SYMBOL = serializers.StringRelatedField(many=True)
    class Meta:
        model = DateBhav
        fields = ['Date', 'SYMBOL']
class SecuritiesSeri(serializers.ModelSerializer):
    class Meta:
        model = Securities
        fields = '__all__'