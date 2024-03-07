from typing import Any, Optional, cast

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self,
        name: str,
        email: str,
        age: int,
        password: Optional[str] = None,
        **kwargs: Any,
    ) -> "User":
        if not email:
            raise ValueError("필수")
        user: "User" = cast("User", self.model(name=name, email=email, age=age))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        name: str,
        email: str,
        age: int,
        password: Optional[str] = None,
        **extra_fields: Any,
    ) -> "User":
        user: "User" = self._create_user(name=name, email=email, age=age, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(verbose_name="email address", unique=True, max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "age"]

    class Meta:
        db_table = "users"

    def is_staff(self) -> bool:
        return self.is_superuser
