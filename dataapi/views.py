from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Datebhavseri, SecuritiesSeri, BhavSeri
from .models import DateBhav, Securities, Bhav
from rest_framework.response import Response

def home(request):
    if request.method=='POST':
        data = request.POST.get('sym')
        obj = Bhav.objects.all().filter(SYMBOL = data)
        if len(obj)<1:
            tri = True
        else:
            tri = False
        return render(request, 'base.html', context={'data':obj, 'tri':tri})
    return render(request, 'base.html')

class DateBhavView(viewsets.ViewSet):
    def list(self, request):
        DaBhavSi = DateBhav.objects.all()
        serializer = Datebhavseri(DaBhavSi, many=True)
        return Response(serializer.data)

class SecuView(viewsets.ViewSet):
    def list(self, request):
        DaBhavSi = Securities.objects.all()
        serializer = SecuritiesSeri(DaBhavSi, many=True)
        return Response(serializer.data)

class BhavView(viewsets.ViewSet):
    def list(self, request):
        DaBhavSi = Bhav.objects.all()
        serializer = BhavSeri(DaBhavSi, many=True)
        return Response(serializer.data)