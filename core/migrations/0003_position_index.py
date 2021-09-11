# Generated by Django 3.2.7 on 2021-09-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_team_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='index',
            field=models.PositiveSmallIntegerField(default=0, help_text='Este campo se utiliza para dar orden de preferencia de aparición. Evitar modificar.', verbose_name='Indice'),
        ),
    ]
