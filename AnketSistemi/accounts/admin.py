from django.contrib import admin
from .forms import UserAdminCreationForm, UserAdminChangeForm
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
        ('Permissions', {'fields': ('ogr', 'hoc', 'yon', 'staff', 'admin',)}),
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


admin.site.register(User, UserAdmin)
# Register your models here.

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
