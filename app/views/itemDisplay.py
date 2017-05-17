from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from ..models import Item, ItemPrice

from django.contrib.auth.decorators import login_required

import json

def itemdisplay(request, id):
    i = Item.objects.get(id=id)

    template = loader.get_template('app/item_display.html')
    context = {
        "item":i
    }
    return HttpResponse(template.render(context, request))


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def loadchart(request, item_id, item_size):

    ip = ItemPrice.objects.filter(item=Item.objects.get(id=item_id),size=item_size)
    results = [ob.as_graph_json() for ob in ip]
    return HttpResponse(json.dumps(results, default=datetime_handler), content_type="application/json")
