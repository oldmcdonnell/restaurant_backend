from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from .models import *

from .serializers import *


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        mutable_data_copy = request.data.copy()
        item_id = mutable_data_copy.get('item')

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class UserCompletedOrdersViewSet(viewsets.ViewSet):
    # action allows the endpoint available to the url
    @action(detail=True, methods=['get'])
    def completed(self, request, pk=None):
        customer = Customer.objects.get(id=id)
        order_history = Order.objects.filter(customer=customer, complete=True)
        serializer = OrderSerializer(order_history, many=True)
        return Response(serializer.data) ##returns filtered data as get response