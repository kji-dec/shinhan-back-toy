from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated

from .serializers import MemberSerializer
from .models import Member

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberDetailView(
    APIView,
):

    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        new_password2 = request.data.get('new_password2')

        if new_password != new_password2:
            return Response({
                "detail": "different new password"
            }, status=status.HTTP_400_BAD_REQUEST)

        member = request.user

        if not check_password(password, member.password):
           return Response({
            "detail": "wrong password"
        }, status=status.HTTP_400_BAD_REQUEST)
            
        member.password = make_password(new_password)
        member.save()

        return Response(status=status.HTTP_200_OK)