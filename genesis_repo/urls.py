from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('genesis_repo.views',
		url(r'^$', 'index', name='index'),
		url(r'^apps/(?P<id>(.+))$', 'apps', name='apps'),
		url(r'^error/', 'error', name='error'),
		url(r'^updates/(?P<id>(.+))$', 'updates', name='updates'),
		url(r'^assets/(?P<id>(.+))$', 'assets', name='assets'),
		url(r'^signatures/(?P<id>(.+))$', 'signatures', name='signatures'),
		url(r'^accounts/', include('registration.backends.default.urls')),
		url(r'^admin/', include(admin.site.urls))
)
