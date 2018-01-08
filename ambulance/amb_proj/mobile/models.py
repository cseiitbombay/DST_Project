from __future__ import unicode_literals

from django.db import models
import datetime

class Hospital(models.Model):
	H_Name = models.CharField(max_length=200)
	H_Phone = models.IntegerField(default=0)
	H_Email = models.EmailField(max_length=50)
	H_Address = models.CharField(max_length=300)
	H_Latitude = models.FloatField(default=0.0)
	H_Longitude = models.FloatField(default=0.0)
	H_LastUpdatedAt = models.DateTimeField('last updated')

	def __str__(self):
		return self.H_Name


class Roadblock(models.Model):
	R_Duration = models.IntegerField(default=0)
	R_Type = models.CharField(max_length=200, default="")
	R_Rating = models.IntegerField(default=0)
	R_Latitude = models.FloatField(default=0.0)
	R_Longitude = models.FloatField(default=0.0)
	R_LastUpdatedAt = models.DateTimeField(default=datetime.datetime.now())
	def __str__(self):
		return self.R_Duration
	

class Specializations(models.Model):
	Specialisation = models.CharField(max_length=50)
	S_LastUpdatedAt = models.DateTimeField('last updated')

	def __str__(self):
		return self.Specialisation


class HospitaltoSpecialization(models.Model):
    Hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    Specialisation = models.ForeignKey(Specializations,on_delete=models.CASCADE)
    
    
    def __unicode__(self):
        return "%s has specialization %s" % (self.Hospital, self.Specialisation)
