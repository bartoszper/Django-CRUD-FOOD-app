from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=50)
    item_price = models.IntegerField(blank=True)

    def __str__(self):
        return self.item_name