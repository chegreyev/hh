from django.conf import settings
from django.db.models import (Model,
                              CharField,
                              TextField,
                              DateField,
                              ForeignKey,
                              CASCADE)
# Token auth / register
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# End Token

UserModel = settings.AUTH_USER_MODEL
# Create your models here.
class Task(Model):
    user = ForeignKey(UserModel , on_delete=CASCADE )
    name = CharField(max_length=255)
    description = TextField()
    creation_date = DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(Model):
    task = ForeignKey(Task, on_delete=CASCADE , related_name='tags')
    name = CharField(max_length=255)
    creation_date = DateField(auto_now_add=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)