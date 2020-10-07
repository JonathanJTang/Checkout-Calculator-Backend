from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    # description = models.TextField()
    # Max price for an item is $1 billion
    price = models.DecimalField(max_digits=12, decimal_places=2)
    taxed_item = models.BooleanField(default=True)
    available_stock = models.IntegerField(default=0)

    def __str__(self):
        return "{}, ${}, Taxed={}, {} available".format(self.name, self.price,
                                                        self.taxed_item,
                                                        self.available_stock)

    # def clean(self):
    #     # data from the form is fetched using super function 
    #     super(Item, self).clean() 
          
    #     # extract the username and text field from the data 
    #     name = self.cleaned_data.get('name') 
    #     price = self.cleaned_data.get('price') 
  
    #     # conditions to be met
    #     if len(name) < 1: 
    #         self._errors['name'] = self.error_class([ 
    #             "Field 'name' must not be empty"]) 
    #     if price < 0: 
    #         self._errors['price'] = self.error_class([ 
    #             "Field 'price' cannot be negative"])
    #         self.add_error('price', "Field 'price' cannot be negative")
  
    #     # return any errors if found 
    #     return self.cleaned_data 