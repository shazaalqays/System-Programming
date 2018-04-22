# Generated by Django 2.0.4 on 2018-04-22 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='00000000', max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Kullanıcı adı')),
                ('ad', models.CharField(default='00000000', max_length=32)),
                ('soyad', models.CharField(default='00000000', max_length=32)),
                ('active', models.BooleanField(default=True, verbose_name='Aktif')),
                ('ogr', models.BooleanField(default=False, verbose_name='Öğrenci')),
                ('hoc', models.BooleanField(default=False, verbose_name='Hoca')),
                ('yon', models.BooleanField(default=False, verbose_name='Yonetim Üyesi')),
                ('staff', models.BooleanField(default=False, verbose_name='Yetkili')),
                ('admin', models.BooleanField(default=False, verbose_name='Admin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='anket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donem', models.CharField(default=None, max_length=1)),
                ('yil', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bolum',
            fields=[
                ('bolum_kodu', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('bolum_adi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ders',
            fields=[
                ('ders_kodu', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('grup_no', models.SmallIntegerField()),
                ('ders_adi', models.CharField(max_length=50)),
                ('teori', models.SmallIntegerField()),
                ('practice', models.SmallIntegerField()),
                ('lab', models.SmallIntegerField()),
                ('toplam_kredi', models.SmallIntegerField()),
                ('donem', models.CharField(default=None, max_length=1)),
                ('yil', models.SmallIntegerField()),
                ('bolum_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.bolum')),
            ],
        ),
        migrations.CreateModel(
            name='ders_anketi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorular', models.CharField(default='111111111111111100000000000000', max_length=30)),
                ('ders_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.ders')),
            ],
        ),
        migrations.CreateModel(
            name='fakulte',
            fields=[
                ('fakulte_kodu', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('fakulte_adi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='fakulte_bolum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolum_kodu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bolum')),
                ('fakulte_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fakulte')),
            ],
        ),
        migrations.CreateModel(
            name='hoca',
            fields=[
                ('hoca_kodu', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=30)),
                ('soyad', models.CharField(max_length=30)),
                ('bolum', models.CharField(max_length=30)),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('bolum_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.bolum')),
            ],
        ),
        migrations.CreateModel(
            name='ogrenci',
            fields=[
                ('ogrenci_no', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ad', models.CharField(max_length=30)),
                ('soyad', models.CharField(max_length=30)),
                ('bolum', models.CharField(max_length=30)),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('bolum_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.bolum')),
            ],
        ),
        migrations.CreateModel(
            name='ogrenci_ders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grup_no', models.SmallIntegerField()),
                ('ders_kodu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.ders')),
                ('ogrenci_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ogrenci')),
            ],
        ),
        migrations.CreateModel(
            name='sonuclar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donem', models.CharField(default=None, max_length=1)),
                ('yil', models.SmallIntegerField()),
                ('grup_no', models.SmallIntegerField()),
                ('katilim_orani', models.FloatField()),
                ('sonuc01', models.FloatField(default=0)),
                ('sonuc02', models.FloatField(default=0)),
                ('sonuc03', models.FloatField(default=0)),
                ('sonuc04', models.FloatField(default=0)),
                ('sonuc05', models.FloatField(default=0)),
                ('sonuc06', models.FloatField(default=0)),
                ('sonuc07', models.FloatField(default=0)),
                ('sonuc08', models.FloatField(default=0)),
                ('sonuc09', models.FloatField(default=0)),
                ('sonuc10', models.FloatField(default=0)),
                ('sonuc11', models.FloatField(default=0)),
                ('sonuc12', models.FloatField(default=0)),
                ('sonuc13', models.FloatField(default=0)),
                ('sonuc14', models.FloatField(default=0)),
                ('sonuc15', models.FloatField(default=0)),
                ('sonuc16', models.FloatField(default=0)),
                ('sonuc17', models.FloatField(default=0)),
                ('sonuc18', models.FloatField(default=0)),
                ('sonuc19', models.FloatField(default=0)),
                ('sonuc20', models.FloatField(default=0)),
                ('sonuc21', models.FloatField(default=0)),
                ('sonuc22', models.FloatField(default=0)),
                ('sonuc23', models.FloatField(default=0)),
                ('sonuc24', models.FloatField(default=0)),
                ('sonuc25', models.FloatField(default=0)),
                ('sonuc26', models.FloatField(default=0)),
                ('sonuc27', models.FloatField(default=0)),
                ('sonuc28', models.FloatField(default=0)),
                ('sonuc29', models.FloatField(default=0)),
                ('sonuc30', models.FloatField(default=0)),
                ('genelsonuc', models.FloatField(default=0)),
                ('ders_kodu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ders')),
            ],
        ),
        migrations.CreateModel(
            name='yonetim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=30)),
                ('soyad', models.CharField(max_length=30)),
                ('makam', models.CharField(max_length=30)),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('bolum_kodu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bolum')),
                ('fakulte_kodu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.fakulte')),
            ],
        ),
        migrations.AddField(
            model_name='ders',
            name='hoca_kodu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.hoca'),
        ),
        migrations.AddField(
            model_name='bolum',
            name='fakulte_kodu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.fakulte'),
        ),
        migrations.AddField(
            model_name='anket',
            name='ders_anketleri',
            field=models.ManyToManyField(to='accounts.ders_anketi'),
        ),
        migrations.AddField(
            model_name='anket',
            name='ogrenci_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.ogrenci'),
        ),
    ]