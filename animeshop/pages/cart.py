import django
from django.http import HttpResponse
from animeshop.modules import wrapper

def cart(request):
    html = f'''<div id="cartTempl"><div class="card bg-black text-white">
  <div class="card-header">
    Shopping cart
  </div>
  <div class="card-body d-flex flex-column gap-3" id="cartcontent">
</div>

  </div>
</div></div>'''
    return HttpResponse(wrapper(html, True, django.middleware.csrf.get_token(request)))