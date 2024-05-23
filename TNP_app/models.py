from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    delivery_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} Delivery instructions {self.delivery_instructions}'

class Food(models.Model):
    TAPAS = 'Tapas'
    EDIBLE = 'Edible'
    GRUEL = 'Gruel'
    ALCOHOL = 'Alcohol'

    CATEGORY = [
        (TAPAS, 'Tapas'),
        (EDIBLE, 'Edible'),
        (GRUEL, 'Gruel'),
        (ALCOHOL, 'Alcohol'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self):
        return f"{self.title} - {self.description} - Type: {self.get_category_display()}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    food_item = models.ManyToManyField(Food, through='OrderItem')

    def __str__(self):
        return f"Order #{self.pk} - Complete: {self.complete}"

    def delivery_instructions(self):
        return self.customer.delivery_instructions

class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.food.title} - Quantity: {self.quantity}"
    
class CustomerReview(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.name} for {self.food.title} - Rating: {self.rating} review {self.review}"