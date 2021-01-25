from django.db import models

# Create your models here.






class Article(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField(max_length=120)

        def __str__(self):
            return self.title
        