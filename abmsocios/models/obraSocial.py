import uuid
from django.db import models


class ObraSocial(models.Model):
    """Medical insurance companies.

    Attributes:
     id_obra(str): primary key of the register for the company.
     nombre(str): name of the medical insurance company.
     nomenclatura(str): nomenclature of the company.
     numero_urgencia(int): telephone number to call the company in
      case of an emergency.

    """
    id_obra = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=50)
    nomenclatura = models.CharField(max_length=10)
    numero_urgencia = models.IntegerField("numero de emergencia")

    def __str__(self):
        return "{}".format(self.nomenclatura)

    class Meta:
        db_table = 'abmsocios_obrasocial'
