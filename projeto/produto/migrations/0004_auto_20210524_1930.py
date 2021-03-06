# Generated by Django 2.2.23 on 2021-05-24 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20191005_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('fornecedor',),
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medida', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('medida',),
            },
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='importado',
            new_name='verificado',
        ),
        migrations.AlterField(
            model_name='produto',
            name='ncm',
            field=models.CharField(max_length=8, verbose_name='Codigo'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.Fornecedor'),
        ),
        migrations.AddField(
            model_name='produto',
            name='medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.Medida'),
        ),
    ]
