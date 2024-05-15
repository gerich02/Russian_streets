from datetime import datetime as dt

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        fields = {'name': 'default',
                  'surname': 'default',
                  'patronymic': 'default',
                  'phone_number': 'default',
                  'birthdate': dt.now(),
                  'city': None,
                  'region': None,
                  'social_network': 'default',
                  'is_staff': True,
                  'passport_series': '0000',
                  'passport_number': '0000',
                  'passport_giver': 'default',
                  'passport_date': dt.now(),
                  'patronymic': 'default',
                  'patronymic': 'default'}
        for field, arg in fields.items():
            extra_fields[field] = arg
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
