from django.db import models
from django.contrib import admin
from dateutil.relativedelta import relativedelta
from datetime import datetime


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class Patients(models.Model):
    first_name = models.CharField("Nombre",max_length=150)
    last_name = models.CharField("Apellido",max_length=150)
    document_number = models.IntegerField(verbose_name="Documento")
    birth_date = models.DateField("Fecha de nacimiento")
    phone_number = models.CharField("Telefono",max_length=150, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    @admin.display(
        description='Nombre completo'
    )
    
    
    def fullname(self):
        return self.__str__()
    
    @property
    @admin.display(
        description='Edad'
    )
    def age(self):
        age = relativedelta(datetime.now(), self.birth_date)
        return age.years

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


