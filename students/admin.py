from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """This is where the admin adds and edits students."""

    list_display = ('student_number', 'last_name', 'first_name', 'program_code',
                    'year_level', 'section', 'status')
    list_filter = ('program_code', 'year_level', 'section', 'status')
    search_fields = ('student_number', 'first_name', 'last_name', 'email')

    fieldsets = (
        ('Academic information', {
            'fields': ('student_number', 'program_code', 'program_name',
                       'year_level', 'section', 'academic_year', 'status'),
        }),
        ('Personal & contact information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'preferred_name',
                       'email', 'phone', 'birth_date', 'city_province', 'address'),
        }),
        ('Family background', {
            'fields': ('father_name', 'mother_name', 'guardian_name',
                       'guardian_relationship', 'guardian_contact'),
        }),
        ('Educational background', {
            'fields': ('elementary_school', 'elementary_year',
                       'high_school', 'high_school_year'),
        }),
    )
