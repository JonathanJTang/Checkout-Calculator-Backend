from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    # description = models.TextField()
    # Max price for an item is $1 billion
    price = models.DecimalField(max_digits=12, decimal_places=2)
    taxed_item = models.BooleanField(default=True)
    available_stock = models.IntegerField(default=0)
    # Discount in dollars, stored as a positive decimal number
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return "{}, ${} (-${} discount), Taxed={}, {} available".format(self.name, 
                                                                        self.price,
                                                                        self.discount,
                                                                        self.taxed_item,
                                                                        self.available_stock)

