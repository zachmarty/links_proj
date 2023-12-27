from typing import Any
from django.core.management import BaseCommand
from user.models import User
class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        email = input()
        user = User.objects.create(
            email = email,
            name = 'admin',
            is_staff = True,
            is_superuser = True,
        )
        
        user.set_password('admin')
        user.save()