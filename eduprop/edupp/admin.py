from django.contrib import admin

from .models import *

admin.site.register(Customer)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(BlogContent)

admin.site.register(ShopLayout)

admin.site.register(Courses)

admin.site.register(CourseLayout)

