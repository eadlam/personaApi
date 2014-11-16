# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('group', models.ForeignKey(to='auth.Group', related_name='messages')),
                ('persona', models.ForeignKey(to='social.Persona', related_name='messages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='persona',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='personas'),
            preserve_default=True,
        ),
    ]
