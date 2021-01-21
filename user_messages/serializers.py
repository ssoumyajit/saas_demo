from rest_framework import serializers
from core.serializers import MyHoodSafeSerializerMixin
from .models import UserMessage


class UserMessageSerializer(MyHoodSafeSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMessage
        fields = (
            'id',
            'url',
            'from_user',
            'to_user',
            'text',
            'date',
        )
