from django.core.management.base import BaseCommand
from TNP_app.models import Customer, Food, Order, OrderItem

class Command(BaseCommand):
    help = 'Create sample orders with provided food and customer data'

    def handle(self, *args, **kwargs):
        # Create food items
        food_data = [
            (1, 'Not Stinky Fish', 'Freshish fish, deep fried with lots of tartar sauce', 5.99, 'Gruel'),
            (2, 'Long Pig', 'Goes great with fava beans and a nice Quiante', 6.99, 'Gruel'),
            (3, 'House Special Gruel', 'Our Famous House Sepcial Gruel', 4.99, 'Gruel'),
            (4, 'Road Kill Gumbo', 'Description of Gruel 3', 5.99, 'Gruel'),
            (5, 'Patatas Bravas', 'Fried potatoes served with a spicy tomato sauce.', 4.99, 'Tapas'),
            (6, 'Gambas al Ajillo', 'Shrimp sautéed in lard.', 8.99, 'Tapas'),
            (7, 'Tortilla Española', 'Spanish omelette made with crow eggs, potatoes, and local greens', 3.99, 'Tapas'),
            (8, 'Calamares a la Romana', 'Fried pig chuckles served with aioli.', 4.99, 'Tapas'),
            (9, 'Mystery Meat Surprise', "You might not want to know what's in it.", 3.99, 'Edible'),
            (10, 'Rubber Chicken', 'Chewy and tasteless, just like grandma used to make.', 4.99, 'Edible'),
            (11, 'Instant Ramen', "For you're weekly dose of sodium.", 2.99, 'Edible'),
            (12, 'Microwave Dinner', "Nuked to perfection, or at least that's what the package claims.", 5.99, 'Edible'),
            (13, 'Cold Beer', 'Ice cold beer.', 2.99, 'Alcohol'),
            (14, 'Well Whiskey', 'Bottom-shelf whiskey that burns on the way down.', 4.99, 'Alcohol'),
            (15, 'House Wine', "Red or white, it's all the same when it comes from a box.", 3.99, 'Alcohol'),
            (16, 'Rotgut Rum', "A pirate's favorite, but not recommended for the faint of heart.", 6.99, 'Alcohol'),
            (17, 'Poitin', 'Brewed in a tin can off the coast of Kerry, guaranteed to make you go blind', 8.99, 'Alcohol'),
        ]

        for item in food_data:
            Food.objects.get_or_create(
                id=item[0],
                defaults={
                    'name': item[1],
                    'description': item[2],
                    'price': item[3],
                    'food_type': item[4],
                }
            )

        # Create customers
        customer_data = [
            (1, 'Quick Draw', 'quickdraw@hhh.com', 'Place it by the mailbox.'),
            (2, 'Gabby Gaelicer', 'noneya@business.com', 'Watch out for the hell hound'),
            (3, 'Dick Fingers', 'Dick@fingers.com', 'Leave at the back door.'),
            (4, 'Le Guiche', 'Le@hGuice.com', 'Under the bridge.'),
            (5, 'Crotch Thumper', 'Crotch@thumper.com', 'Ring the bell and RUUN.'),
            (6, 'Running Bare', 'runningbare@hhh.com', 'Leave by the front door.'),
            (7, 'Pork and Peas Me', 'porkandpeas@hhh.com', 'Drop it near the garage.'),
            (8, 'Zero Dark Squirty', 'zeroSquirt@hhh.com', 'On the porch'),
        ]

        for item in customer_data:
            Customer.objects.get_or_create(
                id=item[0],
                defaults={
                    'name': item[1],
                    'email': item[2],
                    'delivery_instructions': item[3],
                }
            )

        # Create sample orders
        order_data = [
            (1, [1, 2], [2, 1]),
            (2, [3, 4], [1, 2]),
            (3, [5, 6], [1, 1]),
            (4, [7, 8], [2, 1]),
            (5, [9, 10], [1, 2]),
            (6, [11, 12], [1, 1]),
            (7, [13, 14], [1, 1]),
            (8, [15, 16], [1, 1]),
        ]

        for item in order_data:
            customer = Customer.objects.get(id=item[0])
            order = Order.objects.create(customer=customer, complete=False)
            for food_id, quantity in zip(item[1], item[2]):
                food = Food.objects.get(id=food_id)
                OrderItem.objects.create(order=order, food=food, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('Successfully created sample orders'))