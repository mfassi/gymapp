import uuid
from django.db import models
from .socio import Socio


class Telefono(models.Model):
    """Phone number of the member.

    Attributes:
     id_telefono(str): primary key.
     numero(int): phone number.
     tipo(str): indicates whether the contact number
      is personal or is from work.

    """

    PERSONAL = 'PR'
    LABORAL = 'LB'
    tipo_telefono_opciones = (
        (PERSONAL, 'Personal'),
        (LABORAL, 'Laboral'),
    )

    id_telefono = models.UUIDField(primary_key=True,
                                   default=uuid.uuid4,
                                   editable=False)
    numero = models.IntegerField("numero de telefono",
                                 unique=True)
    tipo = models.CharField(max_length=2,
                            choices=tipo_telefono_opciones,
                            default=PERSONAL)
    socio = models.ForeignKey(Socio, null=True)

    def __str__(self):
        return "{} {}".format(self.numero, self.tipo)

    class Meta:
        db_table = 'abmsocios_telefono'
