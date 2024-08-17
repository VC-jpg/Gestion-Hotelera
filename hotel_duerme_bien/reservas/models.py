from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.check_in} to {self.check_out}"
