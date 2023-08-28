from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.

def store(request,category_slug=None):
    # products=None
    
    if category_slug is not None:
        category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(is_available=True,category=category)
        paginator=Paginator(products,1)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
    else:
        category=None
        products=Product.objects.filter(is_available=True)
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        # for i in  paged_products:
        #     print(i)
    categories=Category.objects.all()
    # print(paged_products.has_previous,paged_products.has_next,paged_products.previous_page_number,paged_products.next_page_number)
    context={'products': paged_products, 'categories': categories}
    return render(request, 'store/store.html', context=context)

def product_detail(request,product_slug,category_slug):
    single_product=Product.objects.get(slug=product_slug,category__slug=category_slug)
    return render(request, 'store/product-detail.html',context={'product':single_product})