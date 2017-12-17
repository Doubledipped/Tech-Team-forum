from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

urlpatterns = [
	url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^forum/', include('forum.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
