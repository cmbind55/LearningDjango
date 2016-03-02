from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
)
