from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phonenumber = models.CharField(max_length=122)
    comment = models.TextField(max_length =122)
    date = models.DateField()
    
    def __str__(self):
          return self.name
