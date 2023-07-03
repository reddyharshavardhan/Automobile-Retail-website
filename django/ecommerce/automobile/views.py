from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import django
from.models import *
# Create your views here.

def home(request):
    return render(request,"automobile/index.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,"automobile/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "automobile/products/index.html",context)
    else:
        messages.warning(request,"No such Category")
        return django.redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
                products = Product.objects.filter(slug=prod_slug, status=0).first
                context = {'products':products}
        else:
            messages.error(request, "No such category")
            return django.redirect('collections')

    else:
        messages.error(request, "No such category")
        return django.redirect('collections')
    return render(request, "automobile/products/view.html", context)

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productsList = list(products)
    return JsonResponse(productsList, safe =False)

def searchproduct(request):
    if request.method =='POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm =="":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()

            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, "NO productmatched your search")
                return redirect(request.META.get('HTTP_REFERER'))
    
    return redirect(request.META.get('HTTP_REFERER'))