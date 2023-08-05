from animeshop.functions.db import *

title = 'Anime4U'

def header():
    """
    Header.
    """
    return f'''<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">{title}</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Categories
          </a>
          <ul class="dropdown-menu">
            {getCategories()}
          </ul>
        </li>
        
      <li class="nav-item">
          <a class="nav-link" aria-current="page" href="/cart">Shopping cart</a>
        </li>

      </ul>
    </div>
  </div>
</nav>'''

def footer():
    """
    Footer.
    """
    return f'''
    <div class="d-flex flex-column h-25">
      <div class="container w-100 ms-auto me-auto align-self-end mt-auto">
            <footer class="py-3 my-4">
                <ul class="nav justify-content-center border-bottom pb-3 mb-3 text-white">
                    <li class="nav-item"><a href="/" class="nav-link px-2 text-white">Home</a></li>
                    {getCategoriesFooter()}
                </ul>
                <p class="text-center text-white">© 2022 {title}, Inc</p>
            </footer>
        </div>
    </div>'''

def wrapper(html, centered=False, csrf=''):
    """
    Returns wrapped HTML with navbar, footer, and includes.
    """
    if centered:
        centered ='mt-3 ms-auto me-auto'
    else:
        centered = ''
    return f'''<html>
    <head>
        <script src="/static/cart.js"></script>
        <title>{title}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="title" content="{title}"/>
        <meta name="description" content="Buy some anime toys at {title}!"/>
        <script>
            window.csrftoken = '{csrf}';
        </script>
    </head>
    <body class="bg-dark text-white">
        {header()}
        <div class="ms-3 w-75 {centered}">
            {html}
        </div>
        {footer()}
    </body>
</html>
'''

