from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('webservice.views',
    url(r'setting/add/(?P<category>[a-z]{5,})/(?P<value>[a-z1-9]{3,})', 'add_setting'),
    url(r'setting/delete/(?P<category>[a-z]{5,})/(?P<value>[a-z1-9]{3,})', 'delete_setting'),
    url(r'setting/get/', "get_settings"),

    url(r'files/get/', 'get_files'),
)