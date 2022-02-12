from django.db import models

class Clothes(models.Model):
    type = models.ForeignKey('ClothesType', on_delete=models.CASCADE, blank=True,null=True,)
    size = models.CharField(max_length=50, default=40, blank=False)
    price = models.IntegerField(blank=False, default=15)
    information = models.CharField(max_length=200, blank=True)
    data = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


class ClothesType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)




