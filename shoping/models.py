from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}


class Category (models.Model):
        name = models.CharField(max_length=100, verbose_name='наименование')
        description = models.TextField(max_length=300, verbose_name='описание', **NULLABLE)


        def __str__(self):
           return f"{self.name}"

        class Meta:
                verbose_name = "категория"
                verbose_name_plural = "категории"


class Product (models.Model):

        name = models.CharField(max_length=100, verbose_name='наименование')
        description = models.TextField(max_length=300, verbose_name='описание')
        image = models.ImageField(upload_to="models/", **NULLABLE, verbose_name='изображение')
        category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
        price_for_one = models.IntegerField(default=10, verbose_name='цена за штуку')
        date_of_creatio = models.DateTimeField(auto_now_add=True)
        last_modified_date = models.DateTimeField(auto_now=True)

        def __str__(self):
           return f"{self.name}({self.category}) {self.price_for_one}"

        class Meta:
                verbose_name = "товар"
                verbose_name_plural = "товары"
