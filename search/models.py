from django.db import models


class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Changed to ImageField for handling image uploads
    image = models.ImageField(upload_to='clothing_images/')

    def __str__(self):
        return self.name
