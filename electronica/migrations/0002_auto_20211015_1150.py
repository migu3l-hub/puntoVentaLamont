# Generated by Django 3.2.7 on 2021-10-15 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='electronica.item'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='serie',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.IntegerField(default=0.0, null=True),
        ),
    ]
