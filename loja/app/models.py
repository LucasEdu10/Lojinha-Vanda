from django.db import models


PRODUCT_DISPLAY = (
    ('dis', 'DISPONIVEL'),
    ('ndis', 'NÃO DISPONIVEL')
)

FABRIC_PRINT = (
    ('inf', 'INFORMAR'),
    ('lis', 'LISA'),
    ('cos', 'COM ESTAMPA')
)

def increment_cod():
    last_cod = Fabric.objects.all().order_by('cod_fabric').last()
    if not last_cod:
        return '#' + str(0)
    ultimo_cod = last_cod.cod_fabric
    ultimo_cod = int(ultimo_cod[1:10])
    new_int = ultimo_cod+1
    new_cod = '#' + str(new_int)
    return new_cod

    
class ProductType(models.Model):
    name_product = models.CharField(verbose_name="Nome do Produto", max_length=65)
    
    class Meta():
        verbose_name = (u'Tipo do Produto')
        verbose_name_plural = (u'Tipo dos Produtos')

    def __str__(self):
        return self.name_product
    
class Product(models.Model):
    name_product = models.CharField(verbose_name="Nome do Produto", max_length=65)
    available_product = models.CharField(choices=PRODUCT_DISPLAY, verbose_name="Status do Produto",
                                        default="dis", max_length=30)
    product_type = models.ManyToManyField(ProductType, verbose_name="Tipo do Produto",
                                          related_name="product_type", null=True, blank=True)
    
    class Meta():
        verbose_name = (u'Produto')
        verbose_name_plural = (u'Produtos')

    def __str__(self):
        return self.name_Product

class Fabric(models.Model):
    cod_fabric = models.CharField(max_length=300, default=increment_cod, editable=False)
    name_fabric = models.CharField(verbose_name="Nome do Tecido", max_length=30)
    type_fabric = models.CharField(choices=FABRIC_PRINT, verbose_name="Tipo do tecido",
                                   default="inf", max_length=30)
    available_fabric = models.CharField(choices=PRODUCT_DISPLAY, verbose_name="Status do Tecido",
                                        default="dis", max_length=30)
    description = models.TextField(
        verbose_name="Descrição do Tecido", blank=True, default='')
    
    picture_fabric = models.ImageField(upload_to='images/')
    
    class Meta():
        verbose_name = (u'Tecido')
        verbose_name_plural = (u'Tecidos')

    def __str__(self):
        return self.name_fabric
# Create your models here.
