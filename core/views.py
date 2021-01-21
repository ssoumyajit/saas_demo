from django.core import exceptions


class MyHoodSafeViewMixin:
    """
    this mixin will be used with views that ensures that models are related
    to the Hood during creation and also querysets are filtered for read operations.

    This code abstracts the get_queryset and the perform_create methods since they are
    pretty similar for most views in this project.
    """
    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated()

        myhood_id = self.request.user.myhood_id
        return queryset.filter(myhood_id=myhood_id)

    def perform_create(self, serializer):
        myhood_id = self.request.user.myhood_id
        serializer.save(myhood_id=myhood_id)

