import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "project_tnp.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from TNP_app.models import *



# Food.objects.bulk_create([
#     Food(name='Not Stinky Fish', description='Freshish fish, deep fried with lots of tartar sauce', price=5.99, food_type=Food.GRUEL),
#     Food(name='Long Pig', description='Goes great with fava beans and a nice Quiante', price=6.99, food_type=Food.GRUEL),
#     Food(name='House Special Gruel', description='Our Famous House Sepcial Gruel, ', price=4.99, food_type=Food.GRUEL),
#     Food(name='Road Kill Gumbo', description='Description of Gruel 3', price=5.99, food_type=Food.GRUEL),
# ])

# Food.objects.bulk_create([
#     Food(name='Patatas Bravas', description='Fried potatoes served with a spicy tomato sauce.', price=4.99, food_type=Food.TAPAS),
#     Food(name='Gambas al Ajillo', description='Shrimp sautéed in lard.', price=8.99, food_type=Food.TAPAS),
#     Food(name='Tortilla Española', description='Spanish omelette made with crow eggs, potatoes, and local greens', price=3.99, food_type=Food.TAPAS),
#     Food(name='Calamares a la Romana', description='Fried pig chuckles served with aioli.', price=4.99, food_type=Food.TAPAS),
   
# ])

# Food.objects.bulk_create([
#     Food(name='Mystery Meat Surprise', description='You might not want to know what\'s in it.', price=3.99, food_type=Food.EDIBLE),
#     Food(name='Rubber Chicken', description='Chewy and tasteless, just like grandma used to make.', price=4.99, food_type=Food.EDIBLE),
#     Food(name='Instant Ramen', description='For you\'re weekly dose of sodium.', price=2.99, food_type=Food.EDIBLE),
#     Food(name='Microwave Dinner', description='Nuked to perfection, or at least that\'s what the package claims.', price=5.99, food_type=Food.EDIBLE),

# ])

# Food.objects.bulk_create([
#     Food(name='Cold Beer', description='Ice cold beer.', price=2.99, food_type=Food.ALCOHOL),
#     Food(name='Well Whiskey', description='Bottom-shelf whiskey that burns on the way down.', price=4.99, food_type=Food.ALCOHOL),
#     Food(name='House Wine', description='Red or white, it\'s all the same when it comes from a box.', price=3.99, food_type=Food.ALCOHOL),
#     Food(name='Rotgut Rum', description='A pirate\'s favorite, but not recommended for the faint of heart.', price=6.99, food_type=Food.ALCOHOL),
#     Food(name='Poitin', description='Brewed in a tin can off the coast of Kerry, garauneteed to make you go blind', price=8.99, food_type=Food.ALCOHOL),
# ])

# Customer.objects.bulk_create([
    
#     Customer(name='', email='', delivery_instructions=''),
#     Customer(name='', email='', delivery_instructions=''),
#     Customer(name='', email='', delivery_instructions=''),
#     Customer(name='', email='', delivery_instructions=''),
#     Customer(name='', email='', delivery_instructions=''),
#     Customer(name='', email=''),
# ])

# customers = [
#     Customer(name='Gabby Gaelicer', email='noneya@business.com', delivery_instructions='Watch out for the hell hound'),
#     Customer(name="Dick Fingers", email="Dick@fingers.com", delivery_instructions="Leave at the back door."),
#     Customer(name="Le Guiche", email="Le@hGuice.com", delivery_instructions="Under the bridge."),
#     Customer(name="Crotch Thumper", email="Crotch@thumper.com", delivery_instructions="Ring the bell and RUUN."),
#     Customer(name="Running Bare", email="runningbare@hhh.com", delivery_instructions="Leave by the front door."),
#     Customer(name="Pork and Peas Me", email="porkandpeas@hhh.com", delivery_instructions="Drop it near the garage."),
#     Customer(name="Zero Dark Squirty", email="zeroSquirt@hhh.com", delivery_instructions="On the porch"),
# ]

# Customer.objects.bulk_create(customers)

# customer = Customer.objects.create(
#     name="Quick Draw",
#     email="quickdraw@hhh.com",
#     delivery_instructions="Place it by the mailbox."
# )

# Create a new order for the customer
# order = Order.objects.create(customer=customer)

