from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from dataapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("dateBhav", views.DateBhavView, basename='BhavDate')
router.register("Secu", views.SecuView, basename='Securi')
router.register("Bhav", views.BhavView, basename='Bhav')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.home, name='home')
]
