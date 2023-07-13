from django.db import models


# Create your models here.

class user_table(models.Model):
    name = models.CharField(max_length=50,help_text='Name')
    contact = models.CharField(max_length=50,help_text='Contact')

    def __str__(self):
        return self.name
