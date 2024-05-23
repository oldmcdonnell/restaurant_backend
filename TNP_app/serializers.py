from rest_framework import serializers
from .models import Customer, Food, Order, OrderItem, CustomerReview

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'delivery_instructions']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'food_type']

class OrderItemSerializer(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())

    class Meta:
        model = OrderItem
        fields = ['id', 'food', 'quantity', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created', 'updated', 'complete', 'items', 'delivery_instructions']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        customer_data = validated_data.pop('customer')

        customer, created = Customer.objects.get_or_create(**customer_data)
        order = Order.objects.create(customer=customer, **validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order

class CustomerReviewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    food = FoodSerializer()

    class Meta:
        model = CustomerReview
        fields = ['id', 'customer', 'food', 'rating', 'review']