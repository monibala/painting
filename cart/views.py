from django.shortcuts import render, redirect
from category.models import category_types
from django.contrib.auth.models import User
from login.models import Customer
from products.models import product
from cart.models import Cart, coupon_code, orderinfo, review
from django.contrib import messages
from datetime import date, datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        quantity = 1
        user = request.user
        product_id = request.GET.get('prod_id')
        prod = product.objects.get(id = product_id)
        
        
        item_already_in_cart = Cart.objects.filter(Q(product=prod.id)& Q(user=request.user)).exists()
        if item_already_in_cart:
            return redirect('show_cart')
        else:
            Cart(user=user,product=prod,quantity=quantity).save()
        return redirect('show_cart')
    else:
        messages.warning(request,'Please Login Or Register.')
        return redirect('login')  
# def cart(request):
#     cart_item = Order.objects.all()
#     context = {'cart_item':cart_item}
#     return render(request, 'cart.html', context)
# def add_to_cart(request):
#     user = request.user
#     if request.user.is_authenticated:
#         res={}
        
#         prod = request.GET.get('product')
#         user = User.objects.get(id=request.user.id)
#         item=product.objects.get(id=prod)
#         check_product = Order.objects.filter(id=prod,user=user)
        
#         quantity = 0
#         if prod!=None:
#             if(len(check_product)>0) :
#                 order_prod = check_product[0]
#                 order_prod.quantity+=1
#                 order_prod.save()
#             else:
#                 check_products, created=Order.objects.get_or_create(user=User.objects.get(id=request.user.id),productid=prod,name=item.product_name,fee=item.price)
#                 # check_products=Order(user=User.objects.get(id=request.user.id),productid=prod)
#                 # check_products.save()
        
            
#             check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
#         return redirect('cart')
#     else:
#         messages.warning(request,'Please Login Or Register.')
#         return redirect('login')   
            

    
@login_required
def checkout(request):
    user = request.user
    addr = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount= 0.0
    shipping_amount = 70.0
    totalamount = 0.0 
    cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        totalamount = amount + shipping_amount

    return render(request,'checkout.html' , {'addr':addr , 'totalamount':totalamount , 'cart_items':cart_items}) 
    # user = User.objects.get(id=request.user.id)
    # order_item = Order.objects.filter(user=user)
    # addr = Customer.objects.filter(user=user)
    # li = []
    # subtotal = 0
    # total = 0
    # shipping_amount = 70.0   
    # for i in order_item:
    #     products = product.objects.filter(id=i.productid)
    #     print(products)
    #     prod = product.objects.get(id=i.productid)
    #     subtotal =int(prod.price)*i.quantity
    #     li.append([products,subtotal,i.quantity])
    #     print(subtotal)
    #     total = int(total) + int(subtotal)
    # totalamount = total + shipping_amount
    # print(li)
    # res = {'data':li, 'total':total, 'totalamount':totalamount, 'addr':addr}
    # Coupon
    # if request.method=='POST':
    #     cou_code=request.POST.get('coupon_code')
    #     if cou_code.isdigit():
    #         cd=coupon_code.objects.filter(code=cou_code)
    #         if len(cd)>0:
    #             cod=coupon_code.objects.get(code=cou_code)
    #             for c in order_item:
    #                 c.coupon=cod.code 
    #                 c.save()
    #             # messages.success(request,'Coupon Applied.')
    #             if cod.valid_date>date.today():
    #                 cd=int((cod.discount*total)/100)
    #                 total=total-cd
    #                 c.total=total
    #                 c.save()
    #                 messages.success(request,'Coupon Applied.')
    #             else:
    #                 messages.warning(request,'Coupon Expire !')
    #                 return  redirect('cart')   
    #         else:
    #                 messages.error(request,'Invalid Coupon !')
    #                 return  redirect('cart')   
    #     else:
    #                 messages.error(request,'Invalid Coupon Code !')
    #                 return  redirect('checkout')
    # Form 
    # if request.method=="POST":
    #     fname=request.POST.get('fname')
    #     lname=request.POST.get('lname')
    #     email=request.POST.get('email')
    #     mob_no=request.POST.get('mob_no')
    #     Address=request.POST.get('Address')
    #     State = request.POST.get('State')
    #     pincode = request.POST.get('pincode')

    #     check = orderinfo(user = User.objects.get(id=request.user.id), fname=fname,lname=lname,email=email,mob_no=mob_no,Address=Address,State=State,pincode=pincode)
    #     print(check)
    #     order_item = Order.objects.filter(user=User.objects.get(id=request.user.id))
    #     order_item.delete()
    #     check.save()
    #     return redirect('pay')
   
    return render(request, 'checkout.html', res)
@login_required
def show_cart(request):


    if request.user.is_authenticated:

        user= request.user
        carts = Cart.objects.filter(user=user)

        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0 
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount
                totalamount = amount + shipping_amount


        
            return render(request,'cart.html',{'carts':carts ,'amount':amount ,'totalamount':totalamount })   

        else:
            return render(request,'empty.html')   

    # if request.user.is_authenticated :
    #     cat = category_types.objects.all()
    #     del_id = request.GET.get('delete')
    #     decr_id = request.GET.get('decrid')
    #     print(del_id)
    #     prod = request.GET.get('product')
    #     user = User.objects.get(id=request.user.id)
    #     check_product = Order.objects.filter(user=user)
    #     if del_id!=None:
        
    #         del_order = product.objects.get(id=del_id) 
    #         del_prod = Order.objects.filter(productid=del_id,user = user)
    #         print(del_prod)
    #         del_prod.delete()
    #     check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
        
    #     li = []
    #     subtotal = 0
    #     total = 0
    #     shipping_amount = 70.0 
    #     for i in check_products:
    #         products = product.objects.filter(id=i.productid)
    #         prod = product.objects.filter(id=i.id)
    #         subtotal =int(prod.price)*i.quantity
    #         li.append([products,subtotal,i.quantity])
            
    #         total = int(total) + int(subtotal)
    #     totalamount = total + shipping_amount
    #     res = {'data':li, 'total':total, 'cat':cat, 'totalamount':totalamount}
    #     return render(request,'cart.html',res) 
    # else:
    #     messages.warning(request,'Please Login Or Register.')
    #     return redirect('login')   
             
     
def decrement(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        decr_id= request.GET.get('decrid')
        print(decr_id)
        if decr_id!=None:
            prod = Cart.objects.get(productid=decr_id,user=user) 
            if (prod.quantity - 1)> 0:
                prod.quantity-=1
                prod.save()
        check_products = Cart.objects.filter(user=User.objects.get(id=request.user.id))
        crt = Cart(quantity=prod.quantity)    
        crt.save()
    return redirect('cart')
    # li = []
    # subtotal = 0
    # total = 0
    # for i in check_products:
    #     products = product.objects.filter(id=i.productid)
    #     prod = product.objects.get(id=i.productid)
    #     subtotal =int(prod.price)*i.quantity
    #     li.append([products,subtotal,i.quantity])
        
    #     total = int(total) + int(subtotal)
    # res = {'data':li, 'total':total}
    # return render(request,'cart.html',res)  
    
def increment(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        incr_id= request.GET.get('incrid')
        if incr_id!=None:
            prod = Cart.objects.get(productid=incr_id,user=user) 
            if (prod.quantity + 1)> 0:
                prod.quantity+=1
                prod.save()
        check_products = Cart.objects.filter(user=User.objects.get(id=request.user.id))
        crt = Cart(quantity=prod.quantity)    
        crt.save()
    return redirect('cart')
    # li = []
    # subtotal = 0
    # total = 0
    # for i in check_products:
    #     products = product.objects.filter(id=i.productid)
    #     prod = product.objects.get(id=i.productid)
    #     subtotal =int(prod.price)*i.quantity
    #     li.append([products,subtotal,i.quantity])
        
    #     total = int(total) + int(subtotal)
    # res = {'data':li, 'total':total}
    # return render(request,'cart.html',res)  
@login_required
def delete(request):
    prod = request.GET.get('remove')
    crt = Cart.objects.filter(user= request.user , product_id = prod)
    crt.delete()

    return redirect('show_cart') 

@login_required
def orders(request):
    op = orderinfo.objects.filter(user=request.user)
    amt =0
    shipping = 70
    for o in op:
        amt=amt+o.total_cost
    pay = amt+shipping
    return render(request,'orders.html' , {'order_placed':op, 'pay':pay})    

@login_required
def update(request):
    prod = request.GET.get('min')
    prod1 = request.GET.get('max')
    user = request.user
   
    crt = Cart.objects.filter(user=user , product_id = prod)
    crt1 = Cart.objects.filter(user=user , product_id = prod1)
    print(crt , crt1)
    if prod!=None:
        # print(prod,'//')
        if len(crt)>0:
            ob=crt[0]
            ob.quantity-=1
            ob.save()
           


    elif prod1!=None:
        if len(crt1)>0:
            ob=crt1[0]
            ob.quantity+=1
            ob.save()
           

    else: 
        crts=Cart(user=User.objects.get(id=request.user),product_id=prod,quantity=1)
        crts.save()

    return redirect('show_cart')   

@login_required
def paymentdone(request):
    userid = request.user.id
    user = User.objects.get(id=request.user.id)
    # custid = request.GET.get('custid')
    print(userid)
    customer = Customer.objects.get(id=userid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        orderinfo(user=user, customer=customer,product=c.product, quantity = c.quantity).save()
        c.delete()

    return redirect('orders')
    