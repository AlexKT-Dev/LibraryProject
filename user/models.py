from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)

from .validators import validate_age


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Username must be an email address!')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self.db)
        return user


class UserModel(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField('Date of birth', validators=[validate_age], default=timezone.now())
    avatar = models.ImageField('Avatar', upload_to='media/avatars/', null=True, blank=True)
    phone_number = models.CharField('Phone number', max_length=13, blank=True)
    phone_confirmed = models.PositiveIntegerField('Confirmed', default=0000)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    objects = UserManager()

    def get_absolute_urs(self):
        return '/users/%i/' % (self.pk)
