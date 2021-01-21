from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers
from core.views import MyHoodSafeViewMixin

User = get_user_model()


class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


class UserList(MyHoodSafeViewMixin, generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    """
    # replace this code by using core.views MyHoodSafeMixin
    
    def perform_create(self, serializer):
        myhood_id = self.request.user.myhood_id
        serializer.save(myhood_id=myhood_id)

    def get_queryset(self):
        # ensure that the users belong to the company of user that is making the request
        myhood_id = self.request.user.myhood_id
        return super().get_queryset().filter(myhood_id=myhood_id)
    """


class UserDetail(MyHoodSafeViewMixin, generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    """
    def get_queryset(self):
        
        # ensure that the user belongs to the company of the user that is making the request
        # this method is similar to the one in UserList
        myhood_id = self.request.user.myhood_id
        return super().get_queryset().filter(myhood_id=myhood_id)
    """


class MyHoodDetail(generics.RetrieveUpdateAPIView):
    name = 'myhood-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.MyHoodSerializer

    def get_object(self):
        """
        ensure that users can only see the hood that they belong to
        """
        return self.request.user.myhood

    """
    We inherit from the CompanySafeViewMixin that we defined before to our UserList 
    and UserDetail views. We also remove the get_queryset and perform_create since 
    these are already implemented in the CompanySafeViewMixin.
    """