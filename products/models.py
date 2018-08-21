from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(default="Enter Description")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images', default='generic_product.png')
    
    def __str__(self):
        return self.name