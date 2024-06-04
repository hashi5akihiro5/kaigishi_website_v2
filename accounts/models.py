from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_contribute(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_contribute = True
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_contribute = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Eメールアドレス", max_length=255, unique=True
    )
    is_active = models.BooleanField(default=True)  # 一般ユーザー
    is_contribute = models.BooleanField(default=False)  # 問題投稿者
    is_staff = models.BooleanField(default=False)  # Django Adminサイトへのアクセス権
    is_superuser = models.BooleanField(default=False)  # スーパーユーザー

    username = models.CharField(
        verbose_name="ユーザー名", max_length=100, blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name="名字", max_length=100, blank=True, null=True
    )
    first_name = models.CharField(
        verbose_name="名前", max_length=100, blank=True, null=True
    )

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
