# Generated by Django 4.0 on 2021-12-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]