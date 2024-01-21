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


class Reviews (models.Model):
        title = models.CharField(max_length=100, verbose_name='заголовок' )
        slug = models.CharField(max_length=200, verbose_name='slug',**NULLABLE)
        content = models.TextField(max_length=10000, verbose_name='содержание')
        preview = models.ImageField(upload_to="preview/", **NULLABLE, verbose_name='превью')
        date_of_creation = models.DateTimeField(auto_now_add=True)
        publication_sign = models.BooleanField(default=True, verbose_name='опублекованно')
        number_of_views = models.IntegerField(default=0, verbose_name='просмотры')

        def __str__(self):
                return self.title

        class Meta:
                verbose_name = "отзыв"
                verbose_name_plural = "отзывы"
