from django.contrib import admin
from ecommerceapp.models import  Contact,RoomType,Orders,OrderUpdate, Rating
# Register your models here.
admin.site.register(Contact)
admin.site.register(RoomType)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Rating)
