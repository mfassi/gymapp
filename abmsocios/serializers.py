from rest_framework import serializers
from abmsocios.models.socio import Socio


class ListadoSocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Socio
        fields = ('numero_socio', 'nombre', 'apellido', 
                  'habilitacion', 'documento'
                  )
