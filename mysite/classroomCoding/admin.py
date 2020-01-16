from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Class, Question, ClassStudent

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher',)}),
    )
    list_display = ['email', 'username', 'is_teacher',]

admin.site.register(CustomUser, CustomUserAdmin) #admin.site.register() registers the specific model onto the admin; as practice, try commenting one of these lines out and see how it affects the admin 
admin.site.register(Question)
admin.site.register(Class)
admin.site.register(ClassStudent)
