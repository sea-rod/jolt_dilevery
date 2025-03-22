from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Group


class UserType(models.TextChoices):
    ADMIN_2 = "affliated_admin", "Affliated Admin"
    SHOP_USER = "shop", "Shop User"
    DELIVERY = "delivery", "Delivery Guy"


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20, choices=UserType.choices, default=UserType.SHOP_USER
    )
    is_premium = models.BooleanField(default=False)  # For Shop Users

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.user_type}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    #     self.assign_group_permissions()

    # def assign_group_permissions(self):
    #     """Assigns user to groups based on their user_type."""
    #     group_name = self.user_type
    #     group, _ = Group.objects.get_or_create(name=group_name)
    #     self.groups.add(group)
