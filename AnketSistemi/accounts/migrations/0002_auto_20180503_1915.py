# Generated by Django 2.0.4 on 2018-05-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoca',
            name='bolum',
            field=models.CharField(max_length=50),
        ),
    ]