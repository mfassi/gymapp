import datetime
from django.db import models


class Socio(models.Model):
    """Main information of the new gym member.

    This module generates a new member of the gym.

    Attributes:
      documento(int): id number of the member.
      numero_socio(int): autogenerates a membership identification number
       using the generar_nuevo_socio function.
      nombre(str): first and middle names.
      apellido:(str): last name.
      fecha_nacimiento(date): date of birth.
      foto_perfil(img): uploads a profile image.
      correo(str): email address.
      sexo(): gender selection.
      fecha_inscripcion(date): start date of the membership.
      apto_fisico(bool): indicates if the member has medical authorization
        to do sports.
      fecha_apto(date): date when the medical authorization has being made.
      estado(bool): indicates whether or not the membership is active.

    """

    def generar_numero_socio():
        """Generates a membership number.

        Returns:
         socios_en_base(int): Unique membership number.

        """
        socios_en_base = Socio.objects.count()
        if socios_en_base is None:
            return 1
        else:
            return socios_en_base + 1

    MASCULINO = 'M'
    FEMENINO = 'F'
    sexo_opciones = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino')
    )

    documento = models.IntegerField(primary_key=True)
    numero_socio = models.IntegerField("numero de socio",
                                       unique=True,
                                       editable=False,
                                       default=generar_numero_socio)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField("fecha de nacimiento")
    foto_perfil = models.ImageField("foto de perfil",
                                    upload_to="fotoPerfil/",
                                    blank=True,
                                    null=True)
    correo = models.EmailField(max_length=150)
    sexo = models.CharField(max_length=2,
                            choices=sexo_opciones,
                            default=MASCULINO)
    fecha_inscripcion = models.DateField("fecha de inscripcion",
                                         default=datetime.date.today)
    apto_fisico = models.BooleanField(default=False)
    fecha_apto = models.DateField("fecha de apto fisico",
                                  blank=True,
                                  null=True)
    estado = models.BooleanField(default=True)

    @property
    def nombre_completo(self):
        """Get the full name of the member."""

        return "{} {}".format(self.nombre, self.apellido)

    @property
    def edad(self):
        """Calculates the age of the member.

        Returns:
         age(int): age of the member.

        """

        from dateutil.relativedelta import relativedelta
        age = "{} años".format(
            relativedelta(datetime.date.today(),
                          self.fecha_nacimiento).years
                          )
        return age

    @property
    def habilitacion(self):
        """Get's the status of the membership.

        As the estado field is a boolean, converts the value
        into a string indicating whether the membership
        is active or inactive.

        Returns:
         estado(str): membership status.

        """

        if self.estado:
            return "Activo"
        else:
            return "Inactivo"

    def __str__(self):
        return '{} {}, socio N {}'.format(self.nombre,
                                          self.apellido,
                                          self.numero_socio)

    def get_absolute_url(self):
        return reversed('detalle-socio', args=[str(self.documento)])

    class Meta:
        db_table = 'abmsocios_socio'
