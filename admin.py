import dateutil.parser
import dateutil.relativedelta
import dateutil.utils
import dateutil.zoneinfo
from django.contrib import admin
from .models import Patients, City , Obra_Social , Localidad ,MedicoDerivante ,Diagnostico, \
Consultorio , Profesional ,FichaKinesica ,OrdenDeConsulta ,Turno

# Register your models here.

@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id','fullname',
                    'document_number','birth_date','phone_number',
                    'age', 'city','obra_social','localidad')
    fields = (
        ("first_name","last_name"),
        ("document_number","birth_date","phone_number"),
        ("city","obra_social","localidad")
    )
    search_fields = ("first_name","last_name")
    list_filter = ("id","birth_date","document_number", "city")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", )

@admin.register(Obra_Social)
class Obra_SocialAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("name", )

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ("id","name","codigo_postal")
    search_fields = ("name","codigo_postal")

@admin.register(MedicoDerivante)
class MedicoDerivanteAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("name",)

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("name",)

@admin.register(Consultorio)
class ConsultorioAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone_number')

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','matricula','address','phone_number','localidad')
    fields =(
        ("first_name","last_name"),
        ("matricula","address"),
        ("phone_number","localidad")
        )
    search_fields = ("last_name","localidad")

@admin.register(FichaKinesica)
class FichaKinesicaAdmin(admin.ModelAdmin):
    list_display = ('id','patient','name','start_date','medic','observations','diagnosis')
    fields =(
        ("patient","name"),
        ("start_date","medic"),
        ("observations","diagnosis")
        )
    search_fields = ("patient","name")

@admin.register(OrdenDeConsulta)
class OrdenDeConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','kinesic_sheet','state','sessions_needed','sessions_done',\
                    "start_date","end_date","time")
    fields =(
        ("kinesic_sheet","state"),
        ("sessions_needed","sessions_done"),
        ("start_date","end_date","time")
        )
    search_fields = ("last_name","localidad")

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id','patient','consult_order','state','date','time')

    fields = (
        ("patient","consult_order","state"),
        ("date","time")
        )
    search_fields = ()








