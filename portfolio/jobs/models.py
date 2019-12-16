from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
