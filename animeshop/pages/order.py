from django.http import HttpResponse
from animeshop.modules import wrapper

def order(request):
    return HttpResponse(wrapper('<script>setCart({});</script><h1>Your order is on it\'s way.</h1><h2>We\'ll email you when it will be delievered.</h2><br><br><h4><a href="/">Go back</a></h4>',True))