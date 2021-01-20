from django.db import models, transaction
import uuid
from django.contrib.auth.models import AbstractUser


class MyHoodManager(models.Manager):
    """Manager for Company along with the User and returns them both"""

    @transaction.atomic
    def create_account(self, myhood_name, username, password):

        myhood = MyHood(
            name=myhood_name,
        )
        myhood.save()
        user = User.objects.create_user(
            username=username,
            password=password,
            myhood=myhood,
        )
        return myhood, user


class MyHood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=30)
    objects = MyHoodManager()

    class Meta:
        db_table = 'myhood'

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    myhood = models.ForeignKey(MyHood, related_name='%(class)s', on_delete=models.CASCADE, editable=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'({self.myhood.name}) - {self.username}'


