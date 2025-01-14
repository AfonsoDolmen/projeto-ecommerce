from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    subject = models.CharField(max_length=150, verbose_name='Assunto')
    message = models.TextField(verbose_name='Mensagem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject
