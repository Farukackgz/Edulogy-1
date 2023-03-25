from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index , name='index'),
    path("events/" , views.events , name='events'),
    path("blog1/" , views.blog1 , name='blog1'),
    path("blog2/" , views.blog2 , name='blog2'),
    path("blog3/" , views.blog3 , name='blog3'),
    path("blogsingle/<int:blog_id>" , views.single , name='single'),
    path("blog/" , views.blog , name='blog'),
    path("contact/" , views.contact , name='contact'),
    path("shopsingle/<int:shop_id>" , views.shopsingle , name='shopsingle'),
    path("shop/" , views.shop , name='shop'),
    path("courses/" , views.courses , name='courses'),
    path("cart/" ,views.cart  ,name='cart' ),
    path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]
