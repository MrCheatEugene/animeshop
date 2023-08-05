from django.http import HttpResponse
from animeshop.functions.db import getCard

def membership(request, card):
    if getCard(card)==None:
        return HttpResponse('0', content_type="text/plain")
    return HttpResponse(getCard(card)[1], content_type="text/plain")