from django.contrib import admin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import bolum, fakulte, ogrenci, hoca, ders, yonetim, ders_anketi, sonuclar
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

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

class OgrenciAdmin(admin.ModelAdmin):
    search_fields = ('ogrenci_no',)

    list_display = ('ogrenci_no', 'ad', 'soyad', 'bolum_kodu', 'bolum')


admin.site.register(User, UserAdmin)
admin.site.register(fakulte, FakulteAdmin)
admin.site.register(bolum)
admin.site.register(yonetim)
admin.site.register(hoca)
admin.site.register(ogrenci)
admin.site.register(ders)
admin.site.register(ders_anketi)
admin.site.register(sonuclar)
# Register your models here.

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
