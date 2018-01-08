from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.utils import timezone
from .models import Hospital
from .models import Roadblock
from .models import Specializations
from .models import HospitaltoSpecialization
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import datetime
import ast

def index(request):
	return HttpResponse("Hello, world. You're at the mobile index page.")

@api_view(['GET', 'POST', ])
def registerHospital(request):
	""" register hospital """
	response = {}
	response['success'] = 0
	if request.method == 'POST':
		hospital_name = request.data['H_Name']
		hospital_email = request.data['H_Email']
		hospital_phone = request.data['H_Phone']
		hospital_address = request.data['H_Address']
		hospital_latitude = request.data['H_Latitude']
		hospital_longitude = request.data['H_Longitude']
		hospital_specialization = request.data['H_spl']		
		hospital=Hospital(H_Name = hospital_name,H_Phone=hospital_phone,H_Email=hospital_email,H_Address=hospital_address,H_Latitude=hospital_latitude,H_Longitude=hospital_longitude, H_LastUpdatedAt=datetime.datetime.now())
		hospital_specialization = ast.literal_eval(hospital_specialization)
		hospital.save()
		for specialization in hospital_specialization:
			print specialization
			specialization = Specializations.objects.get(Specialisation=specialization)
			htos=HospitaltoSpecialization(Hospital=hospital,Specialisation=specialization)
			htos.save()
		response['message'] = "Hospital"+hospital_name+" has been added"
		response['success'] = 1
		response['status'] = status.HTTP_200_OK
	else:
		response['message'] = "Sorry wrong place"
		response['success'] = 0
		response['status'] = status.HTTP_403_FORBIDDEN

	return Response(response)

@api_view(['GET', 'POST', ])
def getSpecifications(request):
	response = {}
	allSpecs = Specializations.objects.all()
	specsJS = []
	for s in allSpecs:
		print s
		specsJS.append(s.Specialisation)
	response['specs'] = specsJS
	response['status'] = status.HTTP_200_OK
	return Response(response)

#@csrf_exempt
@api_view(['GET', 'POST', ])
def updateRoadblock(request):
	""" update roadblock """
	response={}
	response['success']=0
	if request.method == 'POST':
		road_duration=request.POST['R_Duration']
		road_type=request.POST['R_Type']
		road_rating=request.POST['R_Rating']
		road_latitude=request.POST['R_Latitude']
		road_longitude=request.POST['R_Longitude']
		road=Roadblock(R_Duration=road_duration,R_Type=road_type,R_Rating=road_rating,R_Latitude=road_latitude,R_Longitude=road_longitude,R_LastUpdatedAt=datetime.datetime.now())
		road.save()
		response['message']="Roadblock"+road_duration+" has been added"
		response['success']=1
	else:
		response['message']="Sorry wrong road"
		response['success']=0

	return JsonResponse(response)

@api_view(['GET', 'POST', ])
def special(request):
	""" specializations """
	response={}
	response['success']=0
	if request.method == 'POST':
		#hosp=request.POST['Hosp_name']
		specialise=request.data['Specialisation']
		specializations = Specializations.objects.filter(Specialisation = specialise)
		if len(specializations) == 0:
			specials=Specializations(Specialisation=specialise,S_LastUpdatedAt=datetime.datetime.now())
			specials.save()
			response['message']="Specializations"+specialise+" has been added"
			response['success']=1
			response['status'] = status.HTTP_200_OK
		else:
			response['message']="Sorry wrong specializations or already present"
			response['success']=0
			response['status'] = status.HTTP_403_FORBIDDEN
	else:
		response['message']="Sorry wrong specializations or already present"
		response['success']=0
		response['status'] = status.HTTP_403_FORBIDDEN

	return Response(response)

#@csrf_exempt
@api_view(['GET', 'POST', ])
def showHospital(request):
	response={}
	if request.method == "POST":
		hospitals=Hospital.objects.all()
		responsef=[]
		for hospital in hospitals:
			response={}
			#response['H_id']=hospital.H_id
			response['H_id']=hospital.id
			response['H_Name']=hospital.H_Name
			response['H_Phone']=hospital.H_Phone
			response['H_Email']=hospital.H_Email
			response['H_Address']=hospital.H_Address
			response['H_Latitude']=hospital.H_Latitude
			response['H_Longitude']=hospital.H_Longitude
			responsef.append(response)
			response['status'] = status.HTTP_200_OK
		#return JsonResponse(dict(hospitals=responsef))
		return Response(response)
	return JsonResponse({'success': 0})
