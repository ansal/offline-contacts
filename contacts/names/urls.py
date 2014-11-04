from django.conf.urls import patterns, include, url

import names.views

urlpatterns = patterns('',

    url(r'^$', names.views.dashboard, name='names_dashboard'),
    url(r'^api/contact/$', names.views.contact, name='names_contact'),
)