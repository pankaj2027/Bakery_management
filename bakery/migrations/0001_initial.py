# Generated by Django 3.1.6 on 2021-04-16 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cost_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_amount', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('bakery_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.bakeryitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='bakery.order')),
            ],
        ),
        migrations.CreateModel(
            name='BakeryItemDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_details', to='bakery.bakeryitem')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.ingredients')),
            ],
        ),
    ]