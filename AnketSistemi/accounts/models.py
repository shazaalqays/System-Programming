from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from .validators import validate_xls_file_extension

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_ogrenci=False,
    is_hoca=False, is_yonetim=False, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User must have a username")
        user_obj = self.model(
            username = username
        )
        user_obj.set_password(password)
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
        return '%s %s' %(self.ad,self.soyad)

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




class fakulteManager(models.Manager):
    def create_fakulte(self, fakultekodu, fakulteadi):
        fakulte = self.create(fakulte_kodu=fakultekodu, fakulte_adi=fakulteadi)
        return fakulte

class fakulte(models.Model):
    fakulte_kodu       = models.CharField(max_length=12,primary_key=True)
    fakulte_adi        = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Fakulteler"



class bolum(models.Model):
    bolum_kodu  = models.CharField(max_length=3, primary_key=True)
    bolum_adi   = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Bölümler"

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
    bolum       = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Öğrenciler"

    def __str__(self):
        return '%s %s' %(self.ad,self.soyad)

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
    bolum       = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Hocalar"

    def __str__(self):
        return self.hoca_kodu

    @property
    def full_name(self):
        return '%s %s' % (self.ad, self.soyad)

class dersdetaylari(models.Model):
    ders_kodu   = models.CharField(max_length=7, primary_key=True)
    ders_adi    = models.CharField(max_length=50)
    teori       = models.SmallIntegerField()
    practice    = models.SmallIntegerField()
    lab         = models.SmallIntegerField()
    toplam_kredi= models.SmallIntegerField()
    acilan_bolum_kodu  = models.ForeignKey(
        bolum,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Ders Detayları"


class ders(models.Model):
    ders_kodu   = models.ForeignKey(
        dersdetaylari,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    grup_no     = models.SmallIntegerField()
    ders_adi    = models.CharField(max_length=50)
    hoca_kodu   = models.ForeignKey(
        hoca,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Dersler"

    def __str__(self):
        return self.ders_adi


class yonetim(models.Model):
    YonetimID     = models.CharField(max_length=8, default=00000000, primary_key=True)
    bolum_kodu   = models.ForeignKey(
        bolum,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    fakulte_kodu = models.ForeignKey(
        fakulte,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    ad          = models.CharField(max_length=30)
    soyad       = models.CharField(max_length=30)
    makam       = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Yönetim"


class kullanici_account(models.Model):
    accountID   = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    ogrenci_no  = models.ForeignKey(
        ogrenci,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    hoca_kodu   = models.ForeignKey(
        hoca,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    yonetim_id   = models.ForeignKey(
        yonetim,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class ogrenci_ders(models.Model):
    ogrenci_no  = models.CharField(max_length=8, default=00000000)
    ders_kodu   = models.CharField(max_length=7, default=0000000)
    grup_no     = models.SmallIntegerField()

    class Meta:
        verbose_name_plural = "Öğrenci_Ders Tablosu"


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

    class Meta:
        verbose_name_plural = "Fakülte_Bölüm Tablosu"


class ders_anketi(models.Model):
    ders_kodu   = models.ForeignKey(
        ders,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    sorular     = models.CharField(max_length=30, default='111111111111111100000000000000')

    class Meta:
        verbose_name_plural = "Ders Anketleri"


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

    class Meta:
        verbose_name_plural = "Anketler"


class sonuclar(models.Model):
    ders_kodu   = models.CharField(max_length=7, default=None)
    ogrenci_no  = models.CharField(max_length=8, default=None)
#    donem           = models.CharField(max_length=1, default=None)
#    yil             = models.SmallIntegerField()
    grup_no         = models.SmallIntegerField()
#    katilim_orani   = models.FloatField()
    sonuc01         = models.FloatField(default=0)
    sonuc02         = models.FloatField(default=0)
    sonuc03         = models.FloatField(default=0)
    sonuc04         = models.FloatField(default=0)
    sonuc05         = models.FloatField(default=0)
    sonuc06         = models.FloatField(default=0)
    sonuc07         = models.FloatField(default=0)
    sonuc08         = models.FloatField(default=0)
    sonuc09         = models.FloatField(default=0)
#    genelsonuc      = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Sonuçlar"


class sorular(models.Model):
    soru           = models.CharField(max_length=512, default=None)

    class Meta:
        verbose_name_plural = "Sorular"

    def __str__(self):
        return self.soru
