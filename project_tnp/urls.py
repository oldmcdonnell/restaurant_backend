"""
URL configuration for project_tnp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TNP_app.views import *

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'food', FoodViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'customer-reviews', CustomerReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('customers/<int:pk>/completed-orders/', UserCompletedOrdersViewSet.as_view({'get':'completed'}), name='customer-completed-orders'),
]