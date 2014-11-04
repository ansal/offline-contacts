from django.conf.urls import patterns, include, url

import names.views

urlpatterns = patterns('',

    url(r'^$', names.views.dashboard, name='names_dashboard'),
    url(r'^api/contact/$', names.views.contact, name='names_contact'),
    url(r'^api/contact/(?P<pk>\d+)/$', names.views.contact_update, name='names_contact_update'),
)