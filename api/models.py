from django.db import models

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()  # Ensure that price is stored as an integer
    image = models.ImageField(upload_to='collection_images/')
    reviews_count = models.IntegerField()  # Correct field name and default value
    description = models.CharField(max_length=500)
    sizes = models.JSONField(null=True, blank=True)  # Corrected field
    description2 = models.CharField(max_length=500)
    related_images = models.ImageField(upload_to='collection_images/')  # Corrected field

    def formatted_price(self):
        return f"${self.price}"  # Ensure price is formatted correctly

    def __str__(self):
        return self.title

class BestSeller(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()  # Ensure that price is stored as an integer
    image = models.ImageField(upload_to='bestseller_images/')

    def __str__(self):
        return self.title
    
    def formatted_price(self):
        return f"${self.price}"

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
    ]

    TYPE_CHOICES = [
        ('Topwear', 'Topwear'),
        ('Bottomwear', 'Bottomwear'),
        ('Winterwear', 'Winterwear'),
    ]

    title = models.CharField(max_length=100)
    price = models.IntegerField()  # Ensure price is an integer
    image = models.ImageField(upload_to='shop_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def formatted_price(self):
        return f"${self.price}"
