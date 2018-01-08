from django.contrib import admin
from .models import Hospital, Specializations, Roadblock, HospitaltoSpecialization

class HospitalName:
	model = Hospital

class HospitalFields(admin.ModelAdmin):
	list_display = ['H_Name', 'H_Phone', 'H_Email', 'H_Address', 'H_Latitude', 'H_Longitude', 'H_LastUpdatedAt']

class RoadblockName:
    model = Roadblock

class RoadblockFields(admin.ModelAdmin):
	list_display = ['R_Duration', 'R_Type', 'R_Rating', 'R_Latitude', 'R_Longitude', 'R_LastUpdatedAt']

class SpecializationsName:
	model = Specializations

class SpecializationsFields(admin.ModelAdmin):
	list_display = ['Specialisation', 'S_LastUpdatedAt']

class HospitaltoSpecializationName:
	model = HospitaltoSpecialization

class HospitaltoSpecializationFields(admin.ModelAdmin):
	list_display = ['Hospital', 'Specialisation']

		
admin.site.register(Hospital, HospitalFields)
admin.site.register(Roadblock, RoadblockFields)
admin.site.register(Specializations, SpecializationsFields)
admin.site.register(HospitaltoSpecialization, HospitaltoSpecializationFields)