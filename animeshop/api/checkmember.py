from django.http import HttpResponse
from animeshop.functions.db import getCard

def checkmember(request, card):
    if getCard(card)==None:
        return HttpResponse('0', content_type="text/plain")
    return HttpResponse('1', content_type="text/plain")