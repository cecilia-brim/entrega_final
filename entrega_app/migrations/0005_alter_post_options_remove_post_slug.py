# Generated by Django 4.0.4 on 2022-07-02 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrega_app', '0004_comentario_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]