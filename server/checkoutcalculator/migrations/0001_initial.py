# Generated by Django 3.1.2 on 2020-10-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('taxed_item', models.BooleanField(default=True)),
                ('available_stock', models.IntegerField(default=0)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=12, default=0.0)),
            ],
        ),
    ]
