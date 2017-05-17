from django.conf.urls import url

from app.views.index import index

urlpatterns = [
    url(r'^$', index, name='appindex'),
]
