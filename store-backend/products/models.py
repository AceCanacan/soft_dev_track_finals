from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    available = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def main_image_url(self):
        if self.main_image and hasattr(self.main_image, 'url'):
            return self.main_image.url
        return ''

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"
