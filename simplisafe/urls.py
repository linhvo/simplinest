from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = [url(r'^$', 'core.views.home', name='home'),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^simplisafe/away', 'core.views.simplisafe_away', name='simplisafe_away'),
               ]
