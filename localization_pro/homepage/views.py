from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your views here.

def home_view(request):
    context = {
        'greeting': _("Welcome to our Localization Project!"),
        'large_number': 12345.67,
        'current_date': timezone.now(),
        'redirect_to': request.path
    }
    return render(request, 'home.html', context)