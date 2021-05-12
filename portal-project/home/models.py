from django.db import models

class News(models.Model):
    text_field = models.TextField()
    image_field = models.ImageField()

    def get_title(self):
    	self.title = self.text_field[:50]
    	return self.title


class DutyForToday(models.Model):
 	kabinet_five = models.CharField(max_length=250)
 	kabinet_four = models.CharField(max_length=250)
 	date = models.DateField()


 	def __str__(self):
 		return str(self.date)
        
 		
    	
    		