from django.conf.urls import patterns, include, url

from django.contrib import admin
from SaAdmin.views import hello

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^saadmin/', include('SaAdmin.urls')),
    url(r'^hello/$', 'SaAdmin.views.hello'),
    url(r'^good/$','SaAdmin.views.current_url_view_good'),
    url(r'^gethost/$','SaAdmin.views.get_host'),
    url(r'^search-form/$','SaAdmin.views.search_form'),
    url(r'^search/$','SaAdmin.views.search'),
    url(r'^contact/$','SaAdmin.views.contact'),
    url(r'^hello2/$','SaAdmin.views.hello2'),
    url(r'^login/$','SaAdmin.views.login'),

)
