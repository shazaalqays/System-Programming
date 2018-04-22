from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_ogrenci=False,
    is_hoca=False, is_yonetim=False, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have a username")
        user_obj = self.model(
            username = username
        )
        user_obj.set_password(username)
        user_obj.ogr        = is_ogrenci
        user_obj.hoc        = is_hoca
        user_obj.yon        = is_yonetim
        user_obj.staff      = is_staff
        user_obj.admin      = is_admin
        user_obj.active     = is_active
        user_obj.save(using = self._db)
        return user_obj

    def create_ogrenci(self, username, password=None):
        ogrenci = self.create_user(
            username,
            is_ogrenci = True
        )
        return ogrenci

    def create_hoca(self, username, password=None):
        hoca = self.create_user(
            username,
            is_hoca = True
        )
        return hoca

    def create_yonetici(self, username, password=None):
        yonetici = self.create_user(
            username,
            is_yonetim = True
        )
        return yonetici

    def create_superuser(self, username, password=None):
        admin = self.create_user(
            username,
            is_staff = True,
            is_admin = True
        )
        return admin


class User(AbstractBaseUser):
    objects = UserManager()

    username    = models.CharField("Kullanıcı adı", default="00000000",
                max_length=8, primary_key=True, unique=True)
    ad          = models.CharField(default="00000000", max_length=32)
    soyad       = models.CharField(default="00000000", max_length=32)
    active      = models.BooleanField("Aktif", default=True)
    ogr         = models.BooleanField("Öğrenci", default=False)
    hoc         = models.BooleanField("Hoca", default=False)
    yon         = models.BooleanField("Yonetim Üyesi", default=False)
    staff       = models.BooleanField("Yetkili", default=False)
    admin       = models.BooleanField("Admin", default=False)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_ogrenci(self):
        return self.ogr

    @property
    def is_hoca(self):
        return self.hoc

    @property
    def is_yonetim(self):
        return self.yon

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

class fakulte(models.Model):
    fakulte_kodu   = models.CharField(max_length=3,primary_key=True)
    fakulte_adi    = models.CharField(max_length=50)


class bolum(models.Model):
    bolum_kodu  = models.CharField(max_length=3, primary_key=True)
    bolum_adi   = models.CharField(max_length=50)
    fakulte_kodu= models.ForeignKey(
        fakulte,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.bolum_adi


class ogrenci(models.Model):
    ogrenci_no  = models.CharField(max_length=8, primary_key=True)
    ad          = models.CharField(max_length=30)
    soyad       = models.CharField(max_length=30)
    bolum_kodu  = models.ForeignKey(
        bolum,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bolum       = models.CharField(max_length=30)
    accountID   = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.ogrenci_no

    @property
    def full_name(self):
        return '%s %s' % (self.ad, self.soyad)

class hoca(models.Model):
    hoca_kodu   = models.CharField(max_length=6, primary_key=True)
    ad          = models.CharField(max_length=30)
    soyad       = models.CharField(max_length=30)
    bolum_kodu  = models.ForeignKey(
        bolum,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bolum       = models.CharField(max_length=30)
    accountID   = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.hoca_kodu

    @property
    def full_name(self):
        return '%s %s' % (self.ad, self.soyad)

class ders(models.Model):
    ders_kodu   = models.CharField(max_length=7, primary_key=True)
    grup_no     = models.SmallIntegerField()
    ders_adi    = models.CharField(max_length=50)
    hoca_kodu   = models.ForeignKey(
        hoca,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bolum_kodu  = models.ForeignKey(
        bolum,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    teori       = models.SmallIntegerField()
    practice    = models.SmallIntegerField()
    lab         = models.SmallIntegerField()
    toplam_kredi= models.SmallIntegerField()
    donem       = models.CharField(max_length=1, default=None)
    yil         = models.SmallIntegerField()

    def __str__(self):
        return self.ders_adi

class yonetim(models.Model):
    bolum_kodu   = models.ForeignKey(
        bolum,
        on_delete=models.CASCADE
    )
    fakulte_kodu = models.ForeignKey(
        fakulte,
        on_delete=models.CASCADE
    )
    accountID   = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    ad          = models.CharField(max_length=30)
    soyad       = models.CharField(max_length=30)
    makam       = models.CharField(max_length=30)

class ogrenci_ders(models.Model):
    ogrenci_no  = models.ForeignKey(
        ogrenci,
        on_delete=models.CASCADE
    )
    ders_kodu   = models.ForeignKey(
        ders,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    grup_no     = models.SmallIntegerField()

class fakulte_bolum(models.Model):
    fakulte_kodu = models.ForeignKey(
        fakulte,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bolum_kodu   = models.ForeignKey(
        bolum,
        on_delete=models.CASCADE
    )

class ders_anketi(models.Model):
    ders_kodu   = models.ForeignKey(
        ders,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    sorular     = models.CharField(max_length=30, default='111111111111111100000000000000')

class anket(models.Model):
    ders_anketleri  = models.ManyToManyField(ders_anketi)
    ogrenci_no      = models.ForeignKey(
        ogrenci,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    donem           = models.CharField(max_length=1, default=None)
    yil             = models.SmallIntegerField()

class sonuclar(models.Model):
    ders_kodu       = models.ForeignKey(
        ders,
        on_delete=models.CASCADE
    )
    donem           = models.CharField(max_length=1, default=None)
    yil             = models.SmallIntegerField()
    grup_no         = models.SmallIntegerField()
    katilim_orani   = models.FloatField()
    sonuc01         = models.FloatField(default=0)
    sonuc02         = models.FloatField(default=0)
    sonuc03         = models.FloatField(default=0)
    sonuc04         = models.FloatField(default=0)
    sonuc05         = models.FloatField(default=0)
    sonuc06         = models.FloatField(default=0)
    sonuc07         = models.FloatField(default=0)
    sonuc08         = models.FloatField(default=0)
    sonuc09         = models.FloatField(default=0)
    sonuc10         = models.FloatField(default=0)
    sonuc11         = models.FloatField(default=0)
    sonuc12         = models.FloatField(default=0)
    sonuc13         = models.FloatField(default=0)
    sonuc14         = models.FloatField(default=0)
    sonuc15         = models.FloatField(default=0)
    sonuc16         = models.FloatField(default=0)
    sonuc17         = models.FloatField(default=0)
    sonuc18         = models.FloatField(default=0)
    sonuc19         = models.FloatField(default=0)
    sonuc20         = models.FloatField(default=0)
    sonuc21         = models.FloatField(default=0)
    sonuc22         = models.FloatField(default=0)
    sonuc23         = models.FloatField(default=0)
    sonuc24         = models.FloatField(default=0)
    sonuc25         = models.FloatField(default=0)
    sonuc26         = models.FloatField(default=0)
    sonuc27         = models.FloatField(default=0)
    sonuc28         = models.FloatField(default=0)
    sonuc29         = models.FloatField(default=0)
    sonuc30         = models.FloatField(default=0)
    genelsonuc      = models.FloatField(default=0)
