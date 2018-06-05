from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	 
    # Examples:
    # url(r'^$', 'etherpadproject.views.home', name='home'),
    # url(r'^etherpadproject/', include('etherpadproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# 
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
     url(r'^', include('etherpadlite.urls')),
  #    url(r'^etherpad', include('etherpadlite.urls')),
	 # url(r'^accounts/profile/$', include('etherpadlite.urls')),
	 # url(r'^logout$', include('etherpadlite.urls')),
	)
