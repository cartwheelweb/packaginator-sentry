from django.conf.urls.defaults import patterns, include, handler500, handler404

urlpatterns = patterns('',
    (r'^', include('sentry.urls')),
)