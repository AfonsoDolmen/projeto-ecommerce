from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    image = models.ImageField(upload_to='media', verbose_name='Imagem')
    price = models.PositiveIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    stock = models.PositiveIntegerField(default=0, verbose_name='Quantidade')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.title
