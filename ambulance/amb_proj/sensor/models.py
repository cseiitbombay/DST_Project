from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sensor(models.Model):
	sensor_id = models.AutoField(primary_key=True)
	sensor_id_name = models.CharField(max_length=40 )
	sen_note = models.CharField(max_length=200)
	sen_active=models.IntegerField(default=0)
	def __str__(self):
		return self.sensor_id_name

class Sensor_Session(models.Model):
	sen_ses_id = models.AutoField(primary_key=True)
	sen_ses_name = models.CharField(max_length=40)
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lon = models.DecimalField(max_digits=9, decimal_places=6)
	on_time = models.DateTimeField('switch on time')
	last_updated = models.DateTimeField('last time')
	ip_add = models.CharField(max_length=12)
	ses_note = models.CharField(max_length=200)
	def __str__(self):
		return self.sen_ses_name

class Session_Data(models.Model):
	ses_data_id = models.AutoField(primary_key=True)
	ses_data_name = models.CharField(max_length=40)
	session_id = models.ForeignKey(Sensor_Session, on_delete=models.CASCADE)
	sound = models.FloatField (default=0)
	co2 = models.FloatField (default=0)
	smoke = models.FloatField (default=0)
	light = models.FloatField (default=0)
	temp = models.FloatField (default=0)
	humidity = models.FloatField (default=0)
	time_rec = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.ses_data_name
