from django.shortcuts import render
from .models import ShopLayout , BlogContent , Courses ,CourseLayout
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

def index(request):
    courselists=Courses.objects.all()
    
    context = {
        'courselists':courselists
        
    }
    return render(request , 'index.html' , context)

    

def events(request):
    return render(request , 'events.html')

def blog1(request):
    bloglists=BlogContent.objects.all()
    return render(request , 'blog-1.html', {'bloglists':bloglists})

def blog2(request):
    bloglists=BlogContent.objects.all()
    return render(request , 'blog-2.html' , {'bloglists':bloglists})

def blog3(request):
    bloglists=BlogContent.objects.all()
    return render(request , 'blog-3.html', {'bloglists':bloglists})

def single(request ,blog_id):
    blog= BlogContent.objects.get(id=blog_id)
    blogall = BlogContent.objects.all()
    context = {
        'blog':blog,
        'blogall':blogall
    }
    return render(request , 'blog-single.html', context)

def blog(request):
    bloglists=BlogContent.objects.all()
    return render(request , 'blog.html' , {'bloglists':bloglists})

def contact(request):
    return render(request , 'page-contact.html')

def courses(request):
    courselist = CourseLayout.objects.all()
    return render(request , 'courses.html' , {'courselist':courselist})    

def shopsingle(request, shop_id):
    shop= ShopLayout.objects.get(id=shop_id)
    shoplist = ShopLayout.objects.all()
    context = {
        'shop':shop,
        'shoplist':shoplist
    }
    return render(request , 'shop-single.html', context)

# def shop(request):
#     shoplist = ShopLayout.objects.all()
#     return render(request , 'shop.html' , {'shoplist':shoplist})   

def shop(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = ShopLayout.objects.all()
    
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'shop.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)    








def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = ShopLayout.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
   