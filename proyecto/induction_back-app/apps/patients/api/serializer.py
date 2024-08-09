from rest_framework import serializers
from ..models import Patients, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name"]

class PatientsSerializer(serializers.ModelSerializer):
    city_data = CitySerializer(source="city", read_only=True )
    class Meta:
        model = Patients
        fields = ["first_name","last_name","fullname","age",\
            "document_number","birth_date","phone_number",\
            "city","obra_social","localidad", "city_data"]


