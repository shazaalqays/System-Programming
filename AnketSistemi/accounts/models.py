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

class bolum(models.Model):
    bolum_kodu  = models.SmallIntegerField(primary_key=True)
    bolum_adi   = models.CharField(max_length=50)

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
