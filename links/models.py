from django.db import models
from user.models import User

class Link(models.Model):
    link = models.URLField(verbose_name = 'оригинальная ссылка')
    hash_code = models.URLField(verbose_name = 'код', unique = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'пользователь')
