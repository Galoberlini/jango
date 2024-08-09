from django.db import models
from django.contrib import admin
from dateutil.relativedelta import relativedelta
from datetime import datetime 
import datetime

# Create your models here.

class Turno(models.Model):
    class Estado(models.IntegerChoices):
        PENDIENTE = 1, 'Pendiente'
        REALIZADO = 2, 'Realizado'
        CANCELADO = 3, 'Cancelado'
        FALTO = 4, 'Falto'

    consult_order = models.ForeignKey('OrdenDeConsulta', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patients', on_delete=models.CASCADE)
    date = models.DateField("Fecha")
    time = models.TimeField("Hora")
    state = models.IntegerField("Estado",choices=Estado.choices)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} {self.date} {self.time}"
    
    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

class OrdenDeConsulta(models.Model):
    ESTADO_CHOICES = [
        ('EN PROGRESO', 'En Progreso'),
        ('PRESENTADO', 'Presentado'),
        ('COBRADO', 'Cobrado'),
    ]
    
    kinesic_sheet = models.ForeignKey('FichaKinesica', on_delete=models.CASCADE)
    sessions_needed = models.IntegerField("Sesiones totales")
    sessions_done = models.IntegerField("Sesiones hechas",default=0, null=True, blank=True)
    start_date = models.DateField("Fecha de inicio")
    end_date = models.DateField("Fecha de finalizacion")
    state = models.CharField("Estado",max_length=100,choices=ESTADO_CHOICES, null=True, blank=True)
    time = models.TimeField("Horario", null=True, blank=True)

    def __str__(self):
        return f"{self.kinesic_sheet.name}"
    
    class Meta:
        verbose_name = 'Orden de consulta'
        verbose_name_plural = 'Ordenes de consulta'



class FichaKinesica(models.Model):
    patient = models.ForeignKey('Patients', on_delete=models.CASCADE)
    start_date = models.DateField("Fecha de inicio",default=datetime.date.today)
    medic = models.ForeignKey('MedicoDerivante', on_delete=models.DO_NOTHING)
    observations = models.TextField("Observaciones", null=True, blank=True)
    name = models.CharField("Nombre",max_length=100)
    diagnosis = models.ForeignKey('Diagnostico', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ficha kinesica'
        verbose_name_plural = 'Fichas kinesicas'

class Profesional(models.Model):
    first_name = models.CharField("Nombre",max_length=100)
    last_name = models.CharField("Apellido",max_length=100)
    matricula = models.CharField("Apellido",max_length=100, null=True, blank=True)
    address = models.CharField("Direccion",max_length=200)
    phone_number = models.CharField("Telefono",max_length=100)
    localidad = models.ForeignKey('Localidad', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    @admin.display(
        description='Nombre completo'
    )
    
    
    def fullname(self):
        return self.__str__()
    

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

class Consultorio(models.Model):
    name = models.CharField("Consultorio",max_length=200)
    address = models.CharField("Direccion",max_length=250)
    phone_number = models.CharField("Telefono",max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'

class Diagnostico(models.Model):
    name = models.CharField("Diagnostico",max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

class MedicoDerivante(models.Model):
    name = models.CharField("Medico derivante",max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Medico derivante'
        verbose_name_plural = 'Medicos derivantes'

class Localidad(models.Model):
    name = models.CharField("Localidad",max_length=100,unique=True, null=True, blank=True)
    codigo_postal = models.CharField("Codigo Postal",max_length=6)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

class Obra_Social(models.Model):
    name = models.CharField("Obra Social",max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Obra Social'
        verbose_name_plural = 'Obra Sociales'

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
    localidad = models.ForeignKey(Localidad,on_delete=models.DO_NOTHING, null=True, blank=True)
    obra_social = models.ForeignKey(Obra_Social,on_delete=models.DO_NOTHING, null=True, blank=True)

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
        age = relativedelta(datetime.datetime.now(), self.birth_date)
        return age.years

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'