from django.shortcuts import render, redirect
from blog.models import Blog

from category.models import category_types
from products.models import product
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # user = User.objects.get(id=request.user.id)
    cat = category_types.objects.all()
    prod = product.objects.all()
    prod1 = product.objects.filter(category_name__category_name = 'Bundeli art')
    prod2 = product.objects.filter(category_name__category_name = 'New Arrival')
    data = product.objects.all().order_by('category_name')
    context = {'cat':cat, 'prod':prod, 'prod1':prod1, 'prod2':prod2, 'data':data}

    return render(request, 'index.html', context)

def search(request):
    cat = category_types.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
   
        if query:
            
            res = product.objects.filter(product_name__icontains=query)
            return render(request,'products.html',{'prod':res,'cat':cat})
        else:
            print('No information available!!')
            return redirect('index') 
