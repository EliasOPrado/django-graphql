# Generated by Django 3.0.5 on 2021-03-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gqlapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='Sales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='Units',
            field=models.IntegerField(),
        ),
    ]
