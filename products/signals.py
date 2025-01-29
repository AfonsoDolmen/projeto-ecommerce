from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from products.models import (
    Product,
    StockMovement,
    Type,
)


@receiver(post_save, sender=Product)
def add_product_to_stock(sender, instance, **kwargs):
    """
    Cria uma nova entrada e soma na quantidade do produto
    """
    product_exists = Product.objects.filter(
        pk=instance.pk
    ).exists()

    # Cria um novo tipo
    new_type = Type.objects.create(type='IN')

    # Cria uma nova movimentação
    StockMovement.objects.create(
        product=instance,
        type=new_type.pk,
        quantity=instance.quantity,
    )

    if product_exists:
        Product.objects.get(pk=instance.pk).quantity += instance.quantity
        return

@receiver(post_delete, sender=Product)
def subtract_product_from_stock(sender, instance, **kwargs):
    pass
