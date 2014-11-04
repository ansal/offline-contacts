from django.conf.urls import patterns, include, url
from django.contrib import admin

import accounts.urls
import names.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include(accounts.urls)),
    url(r'^names/', include(names.urls)),
)
