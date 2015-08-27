from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^the-only-list-in-the-world/$', views.view_list, name='view_list'),

)
