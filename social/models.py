from django.db import models
from django.contrib.auth.models import User, Group

class Persona(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='personas')
    class Meta:
        app_label = "social"

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    persona = models.ForeignKey(Persona, related_name='messages')
    group = models.ForeignKey(Group, related_name='messages')
    class Meta:
        app_label = "social"

class Device(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    device_id = models.TextField()
    user = models.ForeignKey(User, related_name='devices')
    push_enabled = models.BooleanField(default=True)
    class Meta:
        app_label = "social"