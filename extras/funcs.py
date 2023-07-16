from user_auth.models import UserProfile
from django.contrib.auth import get_user
from user_auth.views import getUser

def get_default_address(request):
        user = UserProfile.objects.get(id = request.user['id'])
        return user.address
# def _get_current_user(self):
#     # Assuming you have access to the request object
#     request = self._get_request_object()

#     if request.user.is_authenticated:
#         return request.user

#     return None

