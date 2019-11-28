from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def create_user(request):
    get_user_model().objects.create_user(
        'name', 'email', 'pass',
    )

    return HttpResponse()
