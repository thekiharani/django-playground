# Generated by Django 4.0 on 2021-12-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
