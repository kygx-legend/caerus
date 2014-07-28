from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'oj.views.home', name='home'),
  url(r'^home$', 'oj.views.home', name='home'),
  url(r'^code$', 'oj.views.code', name='code'),
  url(r'^about$', 'oj.views.about', name='about'),
)

urlpatterns += patterns('',
  url(r'^submit$', 'oj.views.submit', name='submit'),
)

urlpatterns += patterns('',
  url(r'^ajax_get_templates/(?P<language>\d+)/$', 'oj.views.ajax_get_templates', name='ajax_get_templates'),
)
