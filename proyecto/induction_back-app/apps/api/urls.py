from rest_framework import routers 
from apps.patients.api.views import PatientsViewset, CityViewset

#imports

router = routers.DefaultRouter()
router.register(r'patients',PatientsViewset)
router.register("cities", CityViewset)

