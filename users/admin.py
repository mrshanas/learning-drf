from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        *UserAdmin.fieldsets,  # unpacked default admin fieldsets
        (
            'Extended attributes',
            {
                'fields': (
                    'is_manager',
                    'is_employee',
                    'location',
                    'phone_no',
                    'job_id',
                )
            }
        )
    )
    list_display = [
        'email',
        'username',
        'is_staff',
        'location',
        'phone_no',
        'updated_date',
        'job_id',
        'is_manager',
        'is_employee'
    ]
    list_filter = [
        'is_manager',
        'is_employee',
        'is_staff',
        'is_superuser',
        'is_active'
    ]


admin.site.register(User, CustomUserAdmin)
