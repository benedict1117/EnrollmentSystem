from urllib.parse import urlencode

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Student

DEMO_USERNAME = 'demo-admin'


#AUTH

def register(request):
    if request.user.is_authenticated:
        return redirect('students')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('students')
    return render(request, 'students/register.html', {'form': form})


def demo_login(request):
    """Sign in as a throwaway 'admin' user so the work can be checked without registering."""
    user, created = User.objects.get_or_create(username=DEMO_USERNAME)
    if created:
        user.set_unusable_password()
        user.save()
    elif user.has_usable_password() or user.is_staff:
        # Someone made a real account with this name; never log into it without a password.
        return redirect('login')
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('students')


def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------------------------------------------------------- students

@login_required
def students(request):
    q = request.GET.get('q', '').strip()
    year = request.GET.get('year', '')
    section = request.GET.get('section', '')
    selected_id = request.GET.get('id', '')

    everyone = Student.objects.all()
    results = everyone
    if q:
        results = results.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q)
            | Q(middle_name__icontains=q) | Q(preferred_name__icontains=q)
            | Q(student_number__icontains=q)
        )
    if year.isdigit():
        results = results.filter(year_level=int(year))
    if section:
        results = results.filter(section=section)

    selected = None
    if selected_id.isdigit():
        selected = everyone.filter(pk=int(selected_id)).first()

    # Keep the current search/filters when a student is clicked.
    keep = {k: v for k, v in (('q', q), ('year', year), ('section', section)) if v}

    context = {
        'students': results,
        'total': everyone.count(),
        'shown': results.count(),
        'selected': selected,
        'year_choices': Student.YEAR_CHOICES,
        'sections': everyone.order_by('section').values_list('section', flat=True).distinct(),
        'f': {'q': q, 'year': year, 'section': section},
        'qs': urlencode(keep),
    }
    return render(request, 'students/students.html', context)
