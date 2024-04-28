from django.db import models
from django.contrib.auth.models import User
from userapp.models import UserProfile
from bookapp.models import (Book,
                            Genre,
                            Discount,
                            Category,
                            Inventory,
                            Author,
                            Publisher,
                            )
from reviewapp.models import Review
from orderapp.models import Order
from shoppingapp.models import ShoppingCart
