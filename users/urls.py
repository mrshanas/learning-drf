from django.urls import path
# from rest_framework.routers import SimpleRouter

from .views import UserRegister

# router = SimpleRouter()
# router.register('', UserViewset)

# urlpatterns = router.urls

app_name = 'users'

urlpatterns = [
    path('signup', UserRegister.as_view(), name='create'),
]
