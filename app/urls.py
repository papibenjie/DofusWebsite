from django.conf.urls import url

from app.views.index import index
from app.views.itemList import ilist, idatatable
from app.views.itemDisplay import itemdisplay, loadchart
from app.views.account import create_account, create_account_page


urlpatterns = [
    url(r'^create_account_page/$', create_account_page, name='createaccountpage'),
    url(r'^create_account/$', create_account, name='createaccount'),

    url(r'^item_list/$', ilist, name='itemlist'),
    url(r'^item_list/datatable/$', idatatable, name='listdatatable'),
    url(r'^load_chart/(?P<item_id>[0-9]+)/(?P<item_size>[0-9]+)/$', loadchart, name="loadchart"),
    url(r'^$', index, name='appindex'),
    url(r'^display_item/(?P<id>[0-9]+)/$', itemdisplay, name='display'),
]
