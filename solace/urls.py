from django.urls import path
# from .views import (
#     registration_view
# )
from .views import (
    UserRegistrationAPIView,
    ProfRegistrationAPIView
)

urlpatterns = [
    path('register/user', UserRegistrationAPIView.as_view(), name='userRegistration'),
    path('register/prof', ProfRegistrationAPIView.as_view(), name="profRegistration")
]