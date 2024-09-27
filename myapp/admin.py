from django.contrib import admin
from .models import ExtendedUser, Product, Purchase, Return

admin.site.register(ExtendedUser)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Return)
