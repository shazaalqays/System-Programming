# Generated by Django 2.0.4 on 2018-04-24 14:37

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dosyalar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosya', models.FileField(upload_to='dosyalar', validators=[accounts.validators.validate_xls_file_extension])),
            ],
        ),
    ]