from django.contrib import admin
from .models import Customer, Food, Order, OrderItem, CustomerReview

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('customer', 'created', 'updated', 'complete')
    list_filter = ('complete', 'created', 'updated')
    search_fields = ('customer__name', 'customer__email')

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(CustomerReview)
