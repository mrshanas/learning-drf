from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
            Abstract method for creating users and superusers
        """
        if not email:
            raise ValueError('A user must have an email')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
            Creates and saves a user with the given email and password
        """

        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
            Creates a superuser and assign the is_superuser=True
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must be admin')

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must be staff')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=255
    )
    is_manager = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=True)
    location = models.CharField(max_length=150, null=True)
    job_id = models.CharField(max_length=50, null=True)
    phone_no = models.PositiveIntegerField(null=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
