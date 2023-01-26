from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    tel = models.CharField(max_length=32, null=True, blank=True, verbose_name="연락처")
    REQUIRED_FIELDS = ["tel"]
    class Meta:
        db_table = 'shinhan_member'
        verbose_name = '회원'
        verbose_name_plural = '회원'