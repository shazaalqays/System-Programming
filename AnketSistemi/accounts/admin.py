from django.contrib import admin
from .forms import UserAdminCreationForm, UserAdminChangeForm, YonetimForm
from .models import bolum, fakulte, ogrenci, hoca, ders, dersdetaylari, yonetim, ders_anketi, sonuclar, ogrenci_ders, fakulte_bolum, kullanici_account, sorular
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

User = get_user_model()

donemler = (
    ('G', 'GÜZ'),
    ('B', 'BAHAR'),
)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'ogr', 'hoc', 'yon', 'staff', 'admin', 'active')
    list_filter = ('ogr', 'hoc', 'yon', 'staff', 'admin', 'active', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('ad', 'soyad')}),
        ('Permissions', {'fields': ('ogr', 'hoc', 'yon', 'staff', 'active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}),
            ('Personal info', {'fields': ('ad', 'soyad')}),
            ('Permissions', {'fields': ('ogr', 'hoc', 'yon', 'staff', 'admin',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


class FakulteAdmin(admin.ModelAdmin):
    list_display = ('fakulte_kodu', 'fakulte_adi')
    ordering = ('fakulte_kodu',)


class BolumAdmin(admin.ModelAdmin):
    list_display = ('bolum_kodu','bolum_adi')
    ordering = ('bolum_kodu',)


class HocaAdmin(admin.ModelAdmin):
    search_fields = ['hoca_kodu','ad','soyad','bolum']

    list_display = ('hoca_kodu','ad','soyad','bolum_kodu','bolum')
    ordering = ('hoca_kodu',)


class YonetimAdmin(admin.ModelAdmin):
    search_fields = ['ad','soyad','makam']

    form = YonetimForm

    list_display = ('bolum_kodu','fakulte_kodu','ad','soyad','makam')
    ordering = ('makam',)


class OgrenciAdmin(admin.ModelAdmin):
    search_fields = ['ogrenci_no','ad', 'soyad', 'bolum']

    list_display = ('ogrenci_no', 'ad', 'soyad', 'bolum_kodu', 'bolum')


class DersAdmin(admin.ModelAdmin):
    list_display = ('ders_kodu', 'grup_no', 'ders_adi', 'hoca_kodu')
    ordering = ('ders_kodu',)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return DerslerAdminForm
        else:
            return super(DersAdmin, self).get_form(request, obj, **kwargs)


class OgrenciDersResource(resources.ModelResource):
    class Meta():
        model = ogrenci_ders


class OgreciDersAdmin(ImportExportActionModelAdmin):
    list_display = ('ogrenci_no', 'ders_kodu', 'grup_no')
    search_fields = ['ogrenci_no', 'ders_kodu']

    resource_class = OgrenciDersResource
    model = ogrenci_ders


class DersDetaylariAdmin(admin.ModelAdmin):
    search_fields = ['ders_kodu','ders_adi','acilan_bolum_kodu']

    list_display = ('ders_kodu','ders_adi','teori','practice','lab','toplam_kredi','acilan_bolum_kodu')
    ordering = ('ders_kodu',)


class DersAnketiAdmin(admin.ModelAdmin):
    search_fields = ('ders_kodu','sorular')

    list_display = ('ders_kodu',)
    ordering = ('ders_kodu',)


class SonuclarAdmin(admin.ModelAdmin):
    search_fields = ['ders_kodu','ogrenci_no']

    list_display = ('ders_kodu','ogrenci_no')
    ordering = ('ders_kodu',)


class FakulteBolumAdmin(admin.ModelAdmin):
    search_fields = ['fakulte_kodu','bolum_kodu']

    list_display = ('fakulte_kodu','bolum_kodu')
    ordering = ('fakulte_kodu','bolum_kodu')


class KullaniciAccountAdmin(admin.ModelAdmin):
    search_fields = ('accountID',)

    list_display = ('accountID','ogrenci_no','hoca_kodu','yonetim_id')
    ordering = ('accountID',)


class SorularAdmin(admin.ModelAdmin):
    list_display = ('id','soru',)
    ordering = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(fakulte, FakulteAdmin)
admin.site.register(bolum, BolumAdmin)
admin.site.register(yonetim, YonetimAdmin)
admin.site.register(hoca, HocaAdmin)
admin.site.register(ogrenci, OgrenciAdmin)
admin.site.register(ders, DersAdmin)
admin.site.register(dersdetaylari, DersDetaylariAdmin)
#admin.site.register(ders_anketi, DersAnketiAdmin)
admin.site.register(sonuclar, SonuclarAdmin)
admin.site.register(ogrenci_ders, OgreciDersAdmin)
admin.site.register(fakulte_bolum, FakulteBolumAdmin)
#admin.site.register(kullanici_account, KullaniciAccountAdmin)
admin.site.register(sorular, SorularAdmin)
# Register your models here.

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
