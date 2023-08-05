from django.http import HttpResponse
from animeshop.functions.db import getItem

def name(request, item):
    if getItem(item)==None:
        return HttpResponse('Unknown', content_type="text/plain")
    return HttpResponse(getItem(item)[2], content_type="text/plain")