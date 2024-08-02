import dateutil.parser
import dateutil.relativedelta
import dateutil.utils
import dateutil.zoneinfo
from django.contrib import admin
from .models import Patients, City


# Register your models here.

@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id','fullname',
                    'document_number','birth_date','phone_number',
                    'age', 'city')
    fields = (
        ("first_name","last_name"),
        ("document_number","birth_date","phone_number"),
        ("city",)
    )
    search_fields = ("first_name","last_name")
    list_filter = ("id","birth_date","document_number", "city")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", )
