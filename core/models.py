from django.db import models

# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=50)
    datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.message, self.datetime)




