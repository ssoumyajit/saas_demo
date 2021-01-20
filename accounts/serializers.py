from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import MyHood

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'username',
            'password'
        )
        # make sure that the password field is never sent back to the client
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        updated = super().update(instance, validated_data)

        if 'password' in validated_data:
            updated.set_password(validated_data['password'])
            updated.save()
        return updated


class MyHoodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MyHood
        fields = (
            'id',
            'name'
        )


class AccountSerializer(serializers.Serializer):
    """Serializer that has two nested serializers: myhood and user"""

    myhood = MyHoodSerializer()
    user = UserSerializer()

    def create(self, validated_data):
        myhood_data = validated_data['myhood']
        user_data = validated_data['user']

        # call the MyHoodManager method to create the Hood and the User
        myhood, user = MyHood.objects.create_account(
            myhood_name=myhood_data.get('name'),
            username=user_data.get('username'),
            password=user_data.get('password'),
        )

        return {'myhood': myhood, 'user': user}

    def update(self, instance, validated_data):
        """
        Overrides the update method to throw an exception if called.
        We do this because we only want this serializer to be used for account creation.
        After that, an edit can be made directly in the /api/v1/users endpoint
        or in the /api/v1/company endpoint (not implemented yet).
        """
        raise NotImplementedError('cannot call update() on an account')
