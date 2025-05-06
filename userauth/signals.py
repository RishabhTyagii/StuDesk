# userauth/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=User)
def assign_permissions_to_staff(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        # Assign all permissions
        for perm in Permission.objects.all():
            instance.user_permissions.add(perm)
        instance.save()
