# Generated by Django 2.0.4 on 2018-05-05 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180505_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici_account',
            name='ogrenci_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.ogrenci'),
        ),
    ]