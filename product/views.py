from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from product.forms import ProductForm
from product.models import Product
def product_list(request):
    products = Product.objects.all()
    print('***************************************')
    return render( request, 'product/product_list.html', {'products':products,'mydata':[1,2,3] })

def product_detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'product/product_detail.html',{'product':product })

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.published_date = timezone.now()
            product.save()
            return HttpResponseBadRequest(reverse('product:product_detail',args=(product.pk,)))
    else:
        form = ProductForm()
        return render(request,'product/product_new.html', {'form':form})


def product_update(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.published_date = timezone.now()
            product.save()
            return HttpResponseBadRequest(reverse('product:product_list'))
    else:
        product = get_object_or_404(Product,pk=product_id)
        return render(request, 'product/product_update.html',{'form': form})

# Create your views here.
