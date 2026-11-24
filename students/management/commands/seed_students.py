from datetime import date

from django.core.management.base import BaseCommand

from students.models import Student

BSIT = ('BSIT', 'BS Information Technology')

SAMPLE = [
    dict(student_number='01200', first_name='Maria', last_name='Dela Cruz', preferred_name='Maria',
         year_level=1, section='1-A', email='maria.delacruz@example.com',
         birth_date=date(2008, 5, 14), city_province='Quezon City, Metro Manila',
         father_name='Ramon Dela Cruz', mother_name='Elena Santos',
         guardian_name='Elena Dela Cruz', guardian_relationship='Mother', guardian_contact='0917 555 0101',
         elementary_school='Quezon City Elementary School', elementary_year='2020',
         high_school='Quezon City Science High School', high_school_year='2026'),
    dict(student_number='53151', first_name='Miguel', last_name='Ramos', preferred_name='Migs',
         year_level=3, section='3-A', email='miguel.ramos@example.com',
         birth_date=date(2005, 11, 2), city_province='Pasig City, Metro Manila',
         father_name='Antonio Ramos', mother_name='Liza Cruz',
         guardian_name='Liza Ramos', guardian_relationship='Mother', guardian_contact='0917 555 0102',
         elementary_school='Pasig Central Elementary School', elementary_year='2017',
         high_school='Pasig City Science High School', high_school_year='2023'),
    dict(student_number='17320', first_name='Angela', last_name='Tan', preferred_name='Angie',
         year_level=2, section='2-B', email='angela.tan@example.com',
         birth_date=date(2006, 8, 21), city_province='Makati City, Metro Manila',
         father_name='Victor Tan', mother_name='Grace Lim',
         guardian_name='Grace Tan', guardian_relationship='Mother', guardian_contact='0917 555 0103',
         elementary_school='Makati Elementary School', elementary_year='2018',
         high_school='Makati Science High School', high_school_year='2024'),
]


class Command(BaseCommand):
    help = 'Load 3 sample students (matches the design mock-up).'

    def handle(self, *args, **options):
        created = 0
        for data in SAMPLE:
            _, was_created = Student.objects.get_or_create(
                student_number=data['student_number'],
                defaults=dict(program_code=BSIT[0], program_name=BSIT[1],
                              status='Enrolled', academic_year='2026–2027', **data),
            )
            created += was_created
        self.stdout.write(self.style.SUCCESS(f'Seeded {created} new student(s).'))
