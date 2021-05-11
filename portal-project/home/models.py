from django.db import models

class News(models.Model):
    text_field = models.TextField()
    image_field = models.ImageField()

    def get_title(self):
    	self.title = self.text_field[:50]
    	return self.title
    	
    		