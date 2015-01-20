from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplisafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^simplisafe/away', 'core.views.simplisafe_away', name='simplisafe_away'),
    url(r'^simplisafe/login', 'core.views.simplisafe_login', name='simplisafe_login')
)
