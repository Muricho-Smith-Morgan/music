from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class BookSession(models.Model):
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    user_email = models.EmailField(max_length=100)
    learning_mode = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # d = strftime("%d-%m-%Y %H:%M:%S")
        return '{} booked this session on {}'.format(self.username, self.booking_time)