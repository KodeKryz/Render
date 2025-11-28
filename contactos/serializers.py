from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Contacto

class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = [
            "url",
            "id",
            "nombre",
            "telefono",
            "correo",
            "direccion",
            "fecha_creacion",
            "fecha_actualizacion",
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]