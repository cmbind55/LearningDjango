from django.conf.urls import patterns, url, include

from lists import views

urlpatterns = patterns('',
    url(r'^home/$', views.home_page, name='lists')
)