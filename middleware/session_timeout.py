import datetime
from django.conf import settings
from django.shortcuts import redirect

class AutoLogout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Get current time and last activity
        current_datetime = datetime.datetime.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity = datetime.datetime.fromisoformat(last_activity)
            # Check if the difference exceeds timeout
            if (current_datetime - last_activity).seconds > getattr(settings, 'AUTO_LOGOUT_DELAY', 120):
                from django.contrib.auth import logout
                logout(request)
                return redirect('login')  # Or wherever you want to redirect

        # Update last activity timestamp
        request.session['last_activity'] = current_datetime.isoformat()

        return self.get_response(request)
