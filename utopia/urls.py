from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'utopia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'grey_rain.views.register'),
    url(r'^login/', 'grey_rain.views.login'),
    url(r'logout/', 'grey_rain.views.logout'),
    url(r'^myaccount/', 'grey_rain.views.myaccount'),
    url(r'^$', 'grey_rain.views.index'),
)

#----- Addded code from legacy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns();
#----- Added code from legacy