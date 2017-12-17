from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'forum/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'forum/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^reg_error/$', views.registerError, name='register'),
	url(r'^addWebsitePost/$', views.addWebsitePost, name='addPost'),
	url(r'^addAssignmentPost/$', views.addAssignmentPost, name='addPost'),
	url(r'^addSurvivingPost/$', views.addSurvivingPost, name='addPost'),
	url(r'^addLectureSlidesPost/$', views.addLectureSlidesPost, name='addPost'),
	url(r'^addChartsPost/$', views.addChartsPost, name='addPost'),
	url(r'^addBinaryPost/$', views.addBinaryPost, name='addPost'),
	url(r'^profile/$', views.viewProfile, name='profile'),
	url(r'^profile/edit/$', views.editProfile, name='editProfile'),
	url(r'^profile/changePassword/$', views.changePassword, name='changePassword'),
]
