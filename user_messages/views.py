from rest_framework import permissions
from rest_framework import generics
from . import serializers
from .models import UserMessage


class UserMessageList(generics.ListCreateAPIView):
    name = 'usermessage-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def perform_create(self, serializer):
        """
        The perform_create function ensures that the UserMessage is related
        to the company that the current logged in user belongs to.
        """
        myhood_id = self.request.user.myhood_id
        serializer.save(myhood_id=myhood_id)

    def get_queryset(self):
        myhood_id = self.request.user.myhood_id
        return super().get_queryset().filter(myhood_id=myhood_id)


class UserMessageDetail(generics.RetrieveAPIView):
    name = 'usermessage-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def get_queryset(self):
        myhood_id = self.request.user.myhood_id
        return super().get_queryset().filter(myhood_id=myhood_id)