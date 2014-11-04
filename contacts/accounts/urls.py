from django.conf.urls import patterns, include, url

import accounts.views

urlpatterns = patterns('',

    url(r'^register/$', accounts.views.register, name='accounts_register'),
    url(r'^login/$', accounts.views.login, name='accounts_login'),
    url(r'^logout/$', accounts.views.logout, name='accounts_logout'),
    
)