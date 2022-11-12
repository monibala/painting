
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from cart.models import Cart, review
from category.models import category_types
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def products(request):
    cat = category_types.objects.all()
    prod = product.objects.all()
    context = {'cat':cat, 'prod':prod}
    return render(request, 'products.html',context)

def productlist(request):
    cat= category_types.objects.all()
    cat_id = request.GET.get('category')
    print(cat_id) 
    cat_data = category_types.objects.get(category_name=cat_id)
    print(cat_data)  
    data = product.objects.filter(category_name = cat_data)
    print(data)
    context = { 'data':data , 'cat':cat}
    return render(request, 'productlist.html', context)

def category_detail(request,pk):
    cat= category_types.objects.all()
    prod = product.objects.filter(category_name=pk)
    print(prod)
    context={'prod':prod, 'cat':cat}

    return render(request,'products.html',context)   


def productdetail(request,pk):
    data = product.objects.get(pk=pk)
    item_already_in_cart = True
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=data.id)& Q(user=request.user)).exists()
       
        print(item_already_in_cart)
    return render(request,'productdetail.html',{'data':data, 'item_already_in_cart ':item_already_in_cart })   
    # cat= category_types.objects.all()
    # id = request.GET.get('product')
    # rvw=review.objects.all()
    # # Review
    if request.method=='POST':
        if request.user.is_authenticated:
            message=request.POST['message']
            email=request.POST['email']
            name=User.objects.get(id=request.user.id)
            prod=product.objects.get(product_name=id)
            img = prod.image
            print(img)
            rvw=review(name=name,comment=message,email=email,produc_name=prod,image=img)
            rvw.save()
            messages.success(request,'Review Posted Successfully.')
            return redirect('index')
        else:
            
            messages.warning(request,'Please! login or register.')
            return redirect ('index')
    data = product.objects.get(pk=pk)
    context = {'data':data ,'cat':cat,'rvw':rvw}   
    # return render(request,'productdetail.html',context)

def blog_category(request,id):
    
    cats = category_types.objects.get(id=id)
    print(cats)
    prod = product.objects.filter(category_name__category_name = cats)
    print(prod)
    data={'cats':cats ,'prod':prod}
    return render(request,'blog_category.html',data) 
