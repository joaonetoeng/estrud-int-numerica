from django.db import models

class IntNumerica(models.Model):
    descricao = models.CharField(max_length=30)
    l = models.DecimalField(max_digits=5, decimal_places=2)
    discretizar = models.IntegerField()
    p = models.DecimalField(max_digits=5, decimal_places=2)
    m = models.DecimalField(max_digits=5, decimal_places=2)
    h = models.DecimalField(max_digits=5, decimal_places=2)
    q = models.DecimalField(max_digits=5, decimal_places=2)
    ei = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao