from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, test_task_queue, test_task_sleep

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^flower/', include('flower.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^queue/', test_task_queue),
    url(r'^sleep/.*', test_task_sleep),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include (debug_toolbar.urls)),
    ] + urlpatterns
