import uuid
from django.db import models
from .socio import Socio


class Domicilio(models.Model):
    """Adresses off the member.

    Attributes:
     id_domicilio(str): primary key.
     calle(str): route.
     numero(int): street number.
     piso(int): appartment floor.
     departamento(str): apartment identification.
     barrio(str): neighbourhood name.
     localidad(str): city name.
     codigo_postal(str): postal code.
     provincia(str): province name.
     tipo(str): tYpe of address, this field is fill with
      choices from the tipo_domicilio_opciones list.
     socio(fk): existing member whom address belong to.

    """

    tipo_domicilio_opciones = [
        ('PR', 'Personal'),
        ('LB', 'Laboral'),
    ]

    id_domicilio = models.UUIDField(primary_key=True,
                                    default=uuid.uuid4,
                                    editable=False)
    calle = models.CharField(max_length=40)
    numero = models.IntegerField()
    piso = models.IntegerField(blank=True,
                               null=True)
    departamento = models.CharField(max_length=4,
                                    blank=True,
                                    null=True)
    barrio = models.CharField(max_length=30,
                              blank=True,
                              null=True)
    localidad = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=10)
    provincia = models.CharField(max_length=20)
    tipo = models.CharField(max_length=2,
                            choices=tipo_domicilio_opciones,
                            default='PR')
    socio = models.ForeignKey(Socio, null=True)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.calle,
                                          self.numero,
                                          self.piso,
                                          self.departamento,
                                          self.barrio,
                                          self.localidad)

    class Meta:
        db_table = 'abmsocios_domicilio'
