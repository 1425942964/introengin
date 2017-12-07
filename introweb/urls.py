from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'webpage.views.home', name='home'),
	url(r'^courseinfo/$', 'webpage.views.courseinfo', name='courseinfo'),
	url(r'^htmlcss/$', 'webpage.views.htmlcss', name='htmlcss'),
	url(r'^javascript/$', 'webpage.views.javascript', name='javascript'),
	url(r'^modules/$', 'webpage.views.modules', name='modules'),
	url(r'^new/$', 'webpage.views.new', name='new'),
	url(r'^python/$', 'webpage.views.python', name='python'),
	url(r'^resources/$', 'webpage.views.resources', name='resources'),
	url(r'^coreskilldemo/$', 'webpage.views.coreskilldemo', name='coreskilldemo'),
	url(r'^schedule/$', 'webpage.views.schedule', name='schedule'),


    url(r'^admin/$', include(admin.site.urls)),
]
