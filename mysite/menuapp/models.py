from django.db import models

# Create your models here.
class Menus(models.Model):

    content = models.CharField(max_length=20, null=False)
    #name = models.