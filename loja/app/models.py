from django.db import models


FABRIC_DISPLAY = (
    ('dis', 'DISPONIVEL'),
    ('ndis', 'NÃO DISPONIVEL')
)


class Fabric(models.Model):
    name_fabric = models.CharField(verbose_name="Nome do Tecido", max_length=65)
    available_fabric = models.CharField(choices=FABRIC_DISPLAY, verbose_name="Status do Tecido",
                                        default="dis", max_length=30)
    
    class Meta():
        verbose_name = (u'Tecido')
        verbose_name_plural = (u'Tecidos')

    def __str__(self):
        return self.name_fabric
    

# Create your models here.
