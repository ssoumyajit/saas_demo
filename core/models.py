import uuid
from django.db import models


class MyHoodRelatedModel(models.Model):
    """
    Abstract class used by models that belong to a Hood
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    myhood = models.ForeignKey('accounts.MyHood', related_name='%(class)s', on_delete=models.CASCADE, editable=False)

    class Meta:
        abstract = True
