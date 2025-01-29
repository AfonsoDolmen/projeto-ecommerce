from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Categoria de produto
    """
    category = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.category


class Product(models.Model):
    """
    Registro de produtos
    """
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    image = models.ImageField(upload_to='media', verbose_name='Imagem')
    price = models.PositiveIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantidade')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.title


class Type(models.Model):
    """
    Tipos de movimentos (Entrada e Saída)
    """
    TYPE_CHOICES = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Tipo')

    def __str__(self) -> str:
        return self.type


    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class StockMovement(models.Model):
    """
    Registro de movimento de estoque.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='stockMovement',
        verbose_name='Movimento do Estoque'
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        related_name='movementType',
        verbose_name='Tipo'
    )

    quantity = models.PositiveIntegerField(verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return self.product.title


    class Meta:
        verbose_name = 'Movimento de Estoque'
        verbose_name_plural = 'Movimentos'
        ordering = ['-created_at']
