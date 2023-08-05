from django.http import HttpResponse
from animeshop.functions.db import getCategory
from animeshop.functions.db import getItems
from animeshop.modules import wrapper

def category(request, cid):
    category = getCategory(cid)
    if category==None:
        return HttpResponse(wrapper('<h2>Invalid category ID</h2>', True))
    items = getItems(cid)
    cards = ''
    for item in items:
        cards+=f'''<div class="card me-3 ms-3 rounded-2" style="flex: 1 1 250px;">
    <div class="card-body">
      <h5 class="card-title">{item[2]}</h5>
      <p class="card-text">{item[3]} $</p>
      <p class="card-text"><small class="text-body-secondary">Price with Gold membership: <b>{round(int(item[3])*0.85, 2)} $</b></small></p>
    </div>
    <div class="card-body d-flex gap-3 flex-row flex-wrap">
    <button type="button" class="btn btn-outline-primary addtocart" data-item="{item[0]}" onclick="addToCart('{item[0]}')">Add to cart</button>
  </div>
  </div>'''
    html = f'''<h3>Items in {category[1]}</h3><div class="card-group mt-3 gap-3">{cards}</div>'''
    return HttpResponse(wrapper(html, True))