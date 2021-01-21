from rest_framework import serializers


class MyHoodSafeRelatedField(serializers.HyperlinkedRelatedField):
    """
    Ensures that the queryset only returns values for the Hood of the logged in user.
    """

    def get_queryset(self):
        """
        the default queryset of HyperlinkedRelatedField is overridden here.
        """
        request = self.context['request']
        myhood_id = request.user.myhood_id
        return super().get_queryset().filter(myhood_id=myhood_id)


class MyHoodSafeSerializerMixin(object):
    """
    Mixin to be used with HyperlinkedModelSerializer to ensure that
    only company values are returned.
    """
    serializer_related_field = MyHoodSafeRelatedField
