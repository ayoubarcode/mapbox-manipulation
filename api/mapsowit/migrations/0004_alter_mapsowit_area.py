# Generated by Django 3.2.7 on 2021-09-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mapsowit", "0003_alter_mapsowit_image_url_plot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mapsowit",
            name="area",
            field=models.CharField(default="0 ha", max_length=128),
        ),
    ]