from django.conf.urls import patterns, include, url

import accounts.views

urlpatterns = patterns('',

    url(r'^register/$', accounts.views.register, name="accounts_register"),
    
)