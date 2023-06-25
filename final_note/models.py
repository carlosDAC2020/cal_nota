from django.db import models

OPCIONES_CLASIFICACION = [
        ('Milagro', 'Milagro'),
        ('Difícil', 'Difícil'),
        ('Aceptable', 'Aceptable'),
        ('Bien', 'Bien'),
        ('Excelente', 'Excelente'),
        ('Perdido', 'Perdido'),
    ]

class Validacion(models.Model):
    

    fecha = models.DateTimeField(auto_now_add=True)
    nota_c1 = models.FloatField()
    nota_c2 = models.FloatField()
    nota_c3 = models.FloatField()
    clasificacion = models.CharField(max_length=10, choices=OPCIONES_CLASIFICACION)

class Mensaje(models.Model):
    texto = models.TextField()
    clasificacion = models.CharField(max_length=10, choices=OPCIONES_CLASIFICACION)