from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Mapping
from .serializers import MappingSerializer


class MappingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer