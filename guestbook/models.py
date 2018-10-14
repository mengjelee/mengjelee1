from django.db import models
from django.conf import settings
# Create your models here.

class TextMessage(models.Model):
	talker = models.CharField(max_length = 20,blank = False)
	message = models.CharField(max_length = 50,blank = True)
	def __str__(self):
		return self.talker + ' ' + self.message
class TextMessage1(models.Model):
	talker1 = models.CharField(max_length = 10,blank = False)
	message1 = models.CharField(max_length = 10,blank = True)
	def __str__(self):
		return self.talker1 + ' ' + self.message1
