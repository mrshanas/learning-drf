from rest_framework.generics import CreateAPIView

from users.serializers import UserRegisterSerializer


class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer
