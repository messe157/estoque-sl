# Generated by Django 2.2.23 on 2021-05-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0007_auto_20210524_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoqueitens',
            name='preco_pro',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='preco'),
        ),
    ]
