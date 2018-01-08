from django.conf.urls import url
from . import views

app_name = 'mobile'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_hospital/$', views.registerHospital, name='registerHospital'),
    url(r'^get_specifications/$', views.getSpecifications, name='getSpecifications'),
    url(r'^show_hospital/$', views.showHospital, name='showHospital'),
    url(r'^update_roadblocks/$', views.updateRoadblock, name='updateRoadblock'),
    url(r'^hosp_specialisation/$', views.special, name='special'),
 ]