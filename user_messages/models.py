from django.db import models
from django.contrib.auth import get_user_model
from core.models import MyHoodRelatedModel
from django.db.models import Q

User = get_user_model()


class UserMessageManager(models.Manager):

    def get_for_user(self, user):
        """
        Retrieves all messages tht a user either sent or received.
        """
        return self.all().filter(myhood_id=user.myhood_id).filter(Q(from_user=user) | Q(to_user=user))


class UserMessage(MyHoodRelatedModel):
    text = models.TextField('message', blank=False, null=False)
    date = models.DateTimeField('date', auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)

    objects = UserMessageManager()

    class Meta:
        db_table = 'user_messages'
        ordering = ['date']

