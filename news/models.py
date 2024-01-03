from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class New(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=65) #VARCHAR
    description = models.TextField()
    time_to_read = models.IntegerField()
    deprecated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add: Ao ser criado, a data será registrada
    update_at = models.DateTimeField(auto_now=True) # auto_now: Ao ser atualizado, a data será registrada
    cover = models.ImageField(upload_to='news/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )  # on_delete=models.SET_NULL: quando a categoria de referencia for apagada, a new terá o campo "category" como NULL |  # null=True: o campo pode ser null
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    def __str__(self):
        return self.title
     
