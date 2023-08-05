function initCart(){
    if(window.localStorage.getItem('cart') == null){
        window.localStorage.setItem('cart', '{}');
    }
}

async function getPrice(itemId){
    return await (await fetch('/api/price/'+encodeURIComponent(itemId))).text();
}

async function getName(itemId){
    return await (await fetch('/api/name/'+encodeURIComponent(itemId))).text();
}

function getCart(){
    initCart();
    return JSON.parse(window.localStorage.getItem('cart'));
}

function setCart(cart){
    initCart();
    window.localStorage.setItem('cart', JSON.stringify(cart));
}

function addToCart(itemId){
    initCart();
    let cart = getCart();
    if(typeof cart[itemId] != 'undefined'){
        cart[itemId] = {amount: cart[itemId]['amount']+=1};
    }else{
        cart[itemId] = {amount: 1};
    }
    setCart(cart);
    alert('Success!');
}

function rmFromCart(itemId){
    initCart();
    let cart = getCart();
    if(typeof cart[itemId] != 'undefined'){
        let a = cart[itemId]['amount']-1;
        if(a == 0 || a<0){
            cart[itemId] = undefined;
            console.log('removed');
        }else{
            cart[itemId] = {amount: a};
        }
    }else{
        cart[itemId] = undefined;
    }
    setCart(cart);
    alert('Success!');
}

function isInCart(itemId){
    initCart();
    let cart = getCart();
    return typeof cart[itemId] != 'undefined';
}

function updInCart(){
    let items = document.querySelectorAll('.addtocart');
    for (let index = 0; index < items.length; index++) {
        const element = items[index];
        if(isInCart(element.dataset.item)){
            element.innerText = 'Added to cart';
            element.setAttribute('style', '    color: var(--bs-btn-disabled-color);\
            background-color: var(--bs-btn-disabled-bg);\
            border-color: var(--bs-btn-disabled-border-color);\
            opacity: var(--bs-btn-disabled-opacity);');
            element.setAttribute('title','Click to checkout');
            element.onclick=()=>{window.location.href='/cart';};
        }
    }
}

async function showCart(force = 0){
    if((window.location.pathname == '/cart' && window.cartloaded != true) || force ==1){
        document.getElementById('cartTempl').style.display = 'block';
        cards = '';
        cart= getCart();
        i = -1;
        total = 0;
        for (element of Object.keys(cart)){
            itemid = element;
            if(cart[itemid]!=undefined && cart[itemid]['amount']>0){
                let price = (await getPrice(itemid));
                total += cart[itemid]['amount']* price;
                cards+=`<div class="card bg-dark rounded-3">\
                <div class="card-body bg-dark text-white border-dark">\
                <h5 class="card-title">${(await getName(itemid))}</h5>\
                <p class="card-text">${cart[itemid]['amount']* price} $ (${price} $ each)</p>\
                <div class="card-text">${cart[itemid]['amount']} pcs <div class="btn-group ms-3" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-secondary" onclick="addToCart('${itemid}'); showCart(1);">+</button>
                <button type="button" class="btn btn-secondary" onclick="rmFromCart('${itemid}');  showCart(1);">-</button>
                </div></div>
                </div>`;
            }
        }
        cards+=`<div class="card bg-dark rounded-3 mt-3">\
        <div class="card-body bg-dark text-white border-dark">\
          <h5 class="card-title">Total amount: ${total}$</h5>\
          <h5 class="card-title" id="discountamount" style="display:none">Total amount with discount: ?</h5>\
          <form method="POST" action="/order" autocomplete="off">
          <input type="hidden" name="csrfmiddlewaretoken" value="${window.csrftoken}">
          <div class="d-flex flex-row flex-wrap gap-3">
            <div class="mb-3 w-25">
                <label for="email" class="form-label">Email address</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="email" class="form-control" id="email" aria-describedby="emailHelp" required name="email">
            </div>
            <div class="mb-3 w-25">
                <label for="card" class="form-label">Credit/debit card number</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="text" class="form-control" id="card" maxlength="16" required  name="card">
            </div>
            <div class="mb-3 w-25">
                <label for="expiration" class="form-label">Expiration date</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="text" class="form-control" id="expiration"maxlength="5" required name="date">
            </div>
            <div class="mb-3 w-25">
                <label for="cvc" class="form-label">CVC</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="password" class="form-control" id="cvc" maxlength="3" required name="cvc">
            </div>
            <div class="mb-3 w-25">
                <label for="address" class="form-label">Full address</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="text" class="form-control" id="address" required name="address">
            </div>
            <div class="mb-3 w-25">
                <label for="membership" class="form-label">Membership card ID (not required)</label>
                <input autocomplete="off"  readonly
     onfocus="this.removeAttribute('readonly');" type="password" class="form-control" id="membership" maxlength="16" name="membership">
            </div>
            </div>
            <button type="submit" class="btn btn-primary">Check out</button>
        </form>
        </div>`
        setTimeout(()=>{document.getElementById('membership').onchange  = async (e)=>{
            let val = e.target.value;
            let isValid = (await (await fetch(`/api/checkmember/${val}`)).text()) == '1';
            if(!isValid){
                alert("Your membership card has expired, or is not valid!");
            }else{
                let discount = (await (await fetch(`/api/membership/${val}`)).text());
                document.getElementById('discountamount').innerText=document.getElementById('discountamount').innerText.replace('?', (total / 100)*100-discount+' $');
                document.getElementById('discountamount').style.display= 'block';
            }
        }}, 250);
        document.getElementById('cartcontent').innerHTML =  cards;
        window.cartloaded = true;
    }
}

setInterval(updInCart, 450);
setInterval(showCart, 450);