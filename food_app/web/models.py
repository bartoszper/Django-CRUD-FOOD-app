from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=50)
    item_price = models.IntegerField(blank=True)
    item_image = models.CharField(max_length=500, default='https://icon-library.com/images/placeholder-image-icon/placeholder-image-icon-21.jpg')

    def __str__(self):
        return self.item_name