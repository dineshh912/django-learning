from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    """
        This class helps to register custom form with 
        django default admin panel
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id','username', 'age', 'desc','is_staff',] # to tell django what fields need to be display on the list
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age','desc',)}),) # In detail view what fields needs to be there
    add_fieldsets = UserAdmin.add_fieldsets+((None, {'fields': ('age','desc',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
