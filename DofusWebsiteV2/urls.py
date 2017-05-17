from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', auth_views.login,  name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/app'},  name='logout'),
    url(r'^app/', include('app.urls')),
]
