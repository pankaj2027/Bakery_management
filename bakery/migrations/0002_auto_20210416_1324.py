# Generated by Django 3.1.6 on 2021-04-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Total_amount',
            field=models.IntegerField(null=True),
        ),
    ]
