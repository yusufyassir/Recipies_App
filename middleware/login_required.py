from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    PUBLIC_PATHS = [
        settings.LOGIN_URL,    # Allow login page
        '/accounts/signup/',   # Allow signup page
    ]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to LOGIN_URL and static files without authentication
         if not request.user.is_authenticated:
            # Check if the request path is in the allowed public paths
            for path in self.PUBLIC_PATHS:
                if request.path.startswith(path):
                    break
            else:
                return redirect(settings.LOGIN_URL)  # Redirect to login page if not allowed
         return self.get_response(request)