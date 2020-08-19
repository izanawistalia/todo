from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#from django.db import models

class task(models.Model):
    item = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_to_complete = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.item
        