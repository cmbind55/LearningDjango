from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import views as list_views
from lists import urls as list_urls
from accounts import urls as account_urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^lists/', include('lists.urls', namespace="lists")),
    url(r'^lists/', include(list_urls)),
    url(r'^accounts/', include(account_urls)),

)
