from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()  # required

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


