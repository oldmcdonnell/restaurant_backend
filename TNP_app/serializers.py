from rest_framework import serializers
from .models import Customer, Food, Order, OrderItem, CustomerReview

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'delivery_instructions']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'title', 'description', 'price', 'category']

class OrderItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'food', 'quantity', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    customer = CustomerSerializer(read_only=True)
    delivery_instructions = serializers.ReadOnlyField(source='customer.delivery_instructions')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created', 'updated', 'complete', 'items', 'delivery_instructions']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order

class CustomerReviewSerializer(serializers.ModelSerializer):
    food_name = serializers.ReadOnlyField(source='food.title')
    customer_name = serializers.ReadOnlyField(source='customer.name')

    class Meta:
        model = CustomerReview
        fields = ['id', 'customer', 'food', 'customer_name', 'food_name', 'rating', 'review']
