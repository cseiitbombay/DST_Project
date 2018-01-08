from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Sensor, Sensor_Session, Session_Data

class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_id','sensor_id_name','sen_note','sen_active',)
    search_fields = ['sensor_id','sensor_id_name','sen_note','sen_active',]

class Sensor_SessionAdmin(admin.ModelAdmin):
    list_display = ('sen_ses_id','sen_ses_name','sensor','lat','lon','on_time','last_updated','ip_add','ses_note',)
    search_fields = ['sen_ses_id','sen_ses_name','sensor','lat','lon','on_time','last_updated','ip_add','ses_note',]

class Session_DataAdmin(admin.ModelAdmin):
    list_display = ('ses_data_id','ses_data_name','session_id','sound','co2','smoke','light','temp','humidity','time_rec',)
    search_fields = ['ses_data_id','ses_data_name','session_id','sound','co2','smoke','light','temp','humidity','time_rec',]

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Sensor_Session, Sensor_SessionAdmin)
admin.site.register(Session_Data,Session_DataAdmin)
