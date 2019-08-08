from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, test_task_queue

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', admin.site.urls),
    url(r'^queue/', test_task_queue)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include (debug_toolbar.urls)),
    ] + urlpatterns
