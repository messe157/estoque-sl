from django.db import models
from django.urls import reverse_lazy


class Produto(models.Model):
    verificado = models.BooleanField(default=False)
    ncm = models.CharField('Codigo', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    data = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    #Fornecedor inicio
    fornecedor = models.ForeignKey(
        'Fornecedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    #Forncedor fim

    #Unidade de Medida inicio
    medida = models.ForeignKey(
        'Medida',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    #Unidade de Medida fim
    
    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }



class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria

# Fornecedor
class Fornecedor(models.Model):
    fornecedor = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('fornecedor',)

    def __str__(self):
        return self.fornecedor

# Unidade de Medida
class Medida(models.Model):
    medida = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('medida',)

    def __str__(self):
        return self.medida


