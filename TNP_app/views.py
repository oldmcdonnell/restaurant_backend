from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Customer, Food, Order, OrderItem, CustomerReview
from .serializers import CustomerSerializer, FoodSerializer, OrderSerializer, OrderItemSerializer, CustomerReviewSerializer


#this is the fly.io version
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data
        items_data = order_data.pop('items', [])
        
        print("Order Data:", order_data)
        print("Items Data:", items_data)
        
        order_serializer = self.get_serializer(data=order_data)
        if not order_serializer.is_valid():
            print("Order Validation Errors:", order_serializer.errors)
            raise ValidationError(order_serializer.errors)
        
        order = order_serializer.save()
        
        for item_data in items_data:
            item_data['order'] = order.id
            item_serializer = OrderItemSerializer(data=item_data)
            if not item_serializer.is_valid():
                print("OrderItem Validation Errors:", item_serializer.errors)
                raise ValidationError(item_serializer.errors)
            item_serializer.save()
        
        headers = self.get_success_headers(order_serializer.data)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class UserCompletedOrdersViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def completed(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)
        
        order_history = Order.objects.filter(customer=customer, complete=True)
        serializer = OrderSerializer(order_history, many=True)
        return Response(serializer.data)
