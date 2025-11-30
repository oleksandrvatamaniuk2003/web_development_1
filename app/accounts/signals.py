from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'accounts':
        author_group, created = Group.objects.get_or_create(name='Author')
        moderator_group, created = Group.objects.get_or_create(name='Moderator')
        print("Groups 'Author' and 'Moderator' checked/created.")


        