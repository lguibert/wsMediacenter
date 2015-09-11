from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('webservice.views',
                       url(r'settings/add/(?P<category>[a-z]{5,})/(?P<value>[a-z0-9%/:A-Z]{1,})', 'add_setting'),
                       url(r'settings/delete/(?P<category>[a-z]{5,})/(?P<value>[a-z0-9%/:A-Z]{1,})', 'delete_setting'),
                       url(r'settings/?', 'get_settings'),

                       url(r'files/(?P<folders>[a-z0-9\/%:A-Z+]{1,})', 'get_files'),
                       url(r'files/', 'get_files'),

                       )
