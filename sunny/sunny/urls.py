from django.conf.urls import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunny.views.home', name='home'),
	# url(r'^sunny/', include('sunny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)),

	url(r'^word/index/$', 'word.views.index'),
	url(r'^word/search/$', 'word.views.search'),
	url(r'^word/sentence/$', 'word.views.sentence'),
	url(r'^word/word_root/$', 'word.views.word_root'),

	# css
	url(r'^image/(/d).jpg/$',{}),
	# url(r'^image/(+/d).jpg$', 'django.views.static.serve', {'document_root':/srv/ftp/upload/image}),

	url(r'^text/index/$', 'text.views.Index'),
	url(r'^text/addtext/$', 'text.views.AddText'),
)
