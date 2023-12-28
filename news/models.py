from django.db import models

# Create your models here.

class New(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=65) #VARCHAR
    description = models.TextField()
    time_to_read = models.IntegerField()
    deprecated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add: Ao ser criado, a data será registrada
    update_at = models.DateTimeField(auto_now=True) # auto_now: Ao ser atualizado, a data será registrada
    cover = models.ImageField(upload_to='news/covers/%Y/%m/%d/')
