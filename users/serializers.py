from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer


class UserRegisterSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }

    def create(self, validated_data):
        """Create a new user"""
        return get_user_model().objects.create_user(**validated_data)
