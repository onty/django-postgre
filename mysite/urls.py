from django.conf.urls import patterns, include, url
from polls.admin import admin_site
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin_site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)
