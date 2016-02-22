# coding=utf-8
from django.conf.urls import patterns, include, url
from show_time.views import current_datetime, hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'time_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^time/$', current_datetime),
    (r'^time/plus/（\d{1,2}）/$', hours_ahead),
    #url(r'^admin/', include(admin.site.urls)),
)