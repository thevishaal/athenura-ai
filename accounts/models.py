from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("User must have a valid Email address.")
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    profile_img = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Only Superuser have permission to access all data
        if self.is_superuser:
            return True
        return super().has_perm(perm, obj)
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        if self.is_superuser:
            return True
        return super().has_module_perms(app_label)