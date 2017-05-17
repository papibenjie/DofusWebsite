from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from ..models import Item
import json

from django.contrib.auth.decorators import login_required

@login_required
def idatatable(request):

    a = Item.objects.all()
    results = [ob.as_json() for ob in a]
    return HttpResponse(json.dumps(results), content_type="application/json")

@login_required
def ilist(request):

    template = loader.get_template('app/list.html')
    items = Item.objects.all()
    context = {
        'LIST_NAME':"Items",
        'PAGE_TITLE':"Liste",
        'items':items,
    }
    return HttpResponse(template.render(context, request))
