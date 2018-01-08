from django.conf.urls import url

from . import views

app_name = 'sensor'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<sensor_id>[0-9]+)/$', views.sen_details, name='sen_details'),
    # ex: /polls/5/results/
    #url(r'^(?P<session_id>[0-9]+)/$', views.sen_ses_details, name='sen_ses_details'),
    # ex: /polls/5/vote/
    #url(r'^(?P<sensor_id>[0-9]+)/vote/$', views.sen_ses_details, name='vote'),
    url(r'^add_sess_data/$', views.add_sess_data, name='add_sess_data'),
    url(r'^add_sess_data_test/$', views.add_sess_data_test, name='add_sess_data_test'),
    url(r'^test/$', views.test, name='test'),
]
