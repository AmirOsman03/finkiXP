from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, ExamTask


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=ExamTask)
def give_xp_on_task_upload(sender, instance, created, **kwargs):
    if created and instance.uploaded_by:
        try:
            profile = instance.uploaded_by.userprofile
            profile.add_xp(10)
        except UserProfile.DoesNotExist:
            pass