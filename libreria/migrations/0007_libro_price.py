# Generated by Django 4.1 on 2022-08-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0006_libro_resumen"),
    ]

    operations = [
        migrations.AddField(
            model_name="libro",
            name="price",
            field=models.FloatField(blank=True, null=True, verbose_name="Precio"),
        ),
    ]
