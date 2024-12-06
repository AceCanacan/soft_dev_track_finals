from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    available = models.BooleanField(default=True)  # New field added

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"