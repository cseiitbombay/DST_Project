from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Sensor,Sensor_Session,Session_Data
from datetime import datetime
from django.utils import timezone

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def sen_details(request, sensor_id):
	sensor_list = Sensor.objects.all()
	#output = ', '.join([q.sensor for q in sensor_list])
	return HttpResponse(sensor_list)

@csrf_exempt
def add_sess_data(request):
    print request.body   #added
    #data_add = request.POST.get("sen_data", "")  # original
    data_add=request.body  # added
    print data_add
    sensor=Sensor.objects.get(sensor_id=1)
    print sensor
    session = Sensor_Session.objects.filter(sensor=sensor).order_by('-sen_ses_id')[0]
    session.last_updated=datetime.now()
    session.save()
    if(data_add):
        mydata = data_add.split(',')
        print mydata
        a=Session_Data()
        a.ses_data_name=str(sensor.sensor_id_name)+'_'+str(session.sen_ses_id)
        a.session_id=session
        a.sound=mydata[0]
        a.co2=mydata[1]
        a.light=mydata[2]
        a.temp=mydata[3]
        a.smoke=mydata[4]
        a.humidity=0
        a.time_rec= datetime.now()
        session.last_updated = a.time_rec
        session.save()
        print sensor.sen_active
        if(sensor.sen_active==1):
            a.save()

       
        #return HttpResponseRedirect(reverse('sensor:sen_table'))
        return HttpResponse("worked")
    else:
        #return render(request,'sensor/add_data.html')
        return HttpResponse("not worked")

def test(request):
	sensor_data=Sensor.objects.all()
	print sensor_data
	context = {'sensor_data' : sensor_data}
	print context
	return render(request,'sensor/test.html',context)

@csrf_exempt
def add_sess_data_test(request):
    mydata = ['1','2','3','4','5','6']
    sensor=Sensor.objects.get(sensor_id=1)
    print sensor
    session = Sensor_Session.objects.filter(sensor=sensor).order_by('-sen_ses_id')[0]
    session.last_updated=datetime.now()
    session.save()


    if(mydata):
    #     #mydata = data_add.split(',')
        print mydata
        a=Session_Data()
        a.ses_data_name=str(sensor.sensor_id_name)+'_'+str(session.sen_ses_id)
        a.session_id=session
        a.sound=mydata[0]
        a.co2=mydata[1]
        a.light=mydata[2]
        a.temp=mydata[3]
        a.smoke=mydata[4]
        a.humidity=0
        a.time_rec= datetime.now()
        session.last_updated = a.time_rec
        session.save()
        a.save()
       # print 
        

       
    #     #return HttpResponseRedirect(reverse('sensor:sen_table'))
        return HttpResponse("worked")
    # else:
    #     #return render(request,'sensor/add_data.html')
    #     return HttpResponse("not worked")
