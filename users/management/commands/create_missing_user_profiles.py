# users/management/commands/create_missing_user_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Create missing UserProfiles for existing Users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profiles:
            UserProfile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created UserProfile for user {user.username}'))