from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'electrocentro.views.home', name='home'),
    # url(r'^electrocentro/', include('electrocentro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
  

   
    # Uncomment the next line to enable the admin:
  url(r'^$','electro.views.vista_informacion'),

  
  url(r'^media/(?P<path>.*)$','django.views.static.serve',
  	{'document_root':settings.MEDIA_ROOT,}),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
  
)
