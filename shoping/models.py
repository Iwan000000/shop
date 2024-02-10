from django.db import models
from django.conf import settings

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

        is_published = models.BooleanField(default=False, verbose_name="публикация")

        editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='редактор')

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



class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=200, verbose_name='название версии')
    version_indicator = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
            return f'{self.product} {self.version_name}'

    class Meta:
            verbose_name = "версия"
            verbose_name_plural = "версии"


