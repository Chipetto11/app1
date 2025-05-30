
from django.core.paginator import Paginator
#from django.http import Http404
from django.shortcuts import  render, get_list_or_404

from goods.models import Products


def catalog(request, category_slug, page = 1):

    if category_slug == 'all':
        goods = Products.objects.all()

    # --- Не работает так как в уроке...
    # elif len(Products.objects.filter(category__slug = category_slug)) > 0:
    #     goods =  Products.objects.filter(category__slug = category_slug)

    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))


    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,

    }
    
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    context = {
        'title': "Home - Каталог", 
        'product': product
    }


    return render(request, "goods/product.html", context=context)
