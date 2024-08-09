from rest_framework import viewsets
from ..models import Patients , City
from .serializer import PatientsSerializer , CitySerializer
from rest_framework.permissions import IsAuthenticated


class PatientsViewset(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class CityViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
