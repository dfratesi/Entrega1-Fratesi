# Generated by Django 4.1 on 2022-08-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0008_alter_libro_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="nacionalidad",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Nacionalidad"
            ),
        ),
    ]
