from django.db import models


class Student(models.Model):
    YEAR_CHOICES = [
        (1, '1st year'),
        (2, '2nd year'),
        (3, '3rd year'),
        (4, '4th year'),
    ]
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Pending', 'Pending'),
        ('On Leave', 'On Leave'),
        ('Dropped', 'Dropped'),
    ]

    # Academic information
    student_number = models.CharField(max_length=20, unique=True, help_text='e.g. 01200')
    program_code = models.CharField(max_length=20, help_text='e.g. BSIT')
    program_name = models.CharField(max_length=120, help_text='e.g. BS Information Technology')
    year_level = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, default=1)
    section = models.CharField(max_length=20, help_text='e.g. 1-A')
    academic_year = models.CharField(max_length=20, default='2026–2027')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')

    #Personal & contact information
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    preferred_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField('Mobile number', max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city_province = models.CharField('City / province', max_length=120, blank=True)
    address = models.CharField('Home address', max_length=255, blank=True)

    #Family background
    father_name = models.CharField(max_length=120, blank=True)
    mother_name = models.CharField('Mother\'s maiden name', max_length=120, blank=True)
    guardian_name = models.CharField('Guardian / emergency contact', max_length=120, blank=True)
    guardian_relationship = models.CharField(max_length=60, blank=True)
    guardian_contact = models.CharField('Guardian contact number', max_length=30, blank=True)

    #Educational background
    elementary_school = models.CharField(max_length=160, blank=True)
    elementary_year = models.CharField('Elementary year graduated', max_length=10, blank=True)
    high_school = models.CharField(max_length=160, blank=True)
    high_school_year = models.CharField('High school year graduated', max_length=10, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.full_name} ({self.student_number})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def initials(self):
        return f'{self.first_name[:1]}{self.last_name[:1]}'.upper()

    @property
    def program_display(self):
        return f'{self.program_name} ({self.program_code})'

    @property
    def display_preferred(self):
        return self.preferred_name or self.first_name

    @property
    def tone(self):
        """Avatar colour, cycles through 3 tones."""
        return self.pk % 3 if self.pk else 0

    @property
    def list_line(self):
        return f'{self.student_number} · {self.program_code} · {self.section}'

    @property
    def year_and_section(self):
        return f'{self.get_year_level_display()} · {self.section}'
