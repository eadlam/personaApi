from django.contrib.auth.models import User, Group
from personas.social.models import Persona, Message, Device

from rest_framework import serializers


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('url', 'push_enabled', 'device_id', 'user')


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Persona
        fields = ('url', 'name', 'user', 'id')
        write_only_fields = ['user']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Persona
        fields = ('name', 'id')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(source='persona', read_only=True)
    class Meta:
        model = Message
        fields = ('url', 'text', 'persona', 'group', 'created', 'author')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'personas')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('url', 'name', 'messages', 'id')

