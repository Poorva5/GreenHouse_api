# Generated by Django 4.1.4 on 2022-12-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="grow_pot_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="height",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="planter_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]