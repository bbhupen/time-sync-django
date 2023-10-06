from .models import Participant
from django.shortcuts import redirect


def user_login_required(function):
    def wrapper(request, login_url='time_sync:login', *args, **kwargs):
        if not 'user_id' in request.session:
            return redirect(login_url)
        else:
            return function(request, *args, **kwargs)
        
    return wrapper