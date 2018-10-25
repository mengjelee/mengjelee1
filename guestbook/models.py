from django.db import models
from django.conf import settings
# Create your models here.

class TextMessage(models.Model):
	talker = models.CharField(max_length = 20,blank = False)
	message = models.CharField(max_length = 50,blank = True)
	def __str__(self):
		return self.talker + ' ' + self.message
class UserData(models.Model):
    username = models.CharField(max_length = 20,blank = False)
    password = models.CharField(max_length = 20,blank = True)
    def __str__(self):
        return self.username + self.password
