from django.db import models

class News(models.Model):
    text_field = models.CharField(max_length=250)
    image_field = models.ImageField()