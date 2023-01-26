from rest_framework import mixins, generics

from .serializers import MemberSerializer

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)