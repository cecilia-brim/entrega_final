# Generated by Django 4.0.4 on 2022-07-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega_app', '0006_comentario_id_post_alter_comentario_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='id_post',
            field=models.IntegerField(),
        ),
    ]
