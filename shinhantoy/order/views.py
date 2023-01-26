from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import (
    OrderSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
)
from .models import Order, Comment

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class CommentListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id)\
                    .select_related('order')\
                    .order_by('-id')
        return Comment.objects.none()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class CommentDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.all().order_by('id')
    
    def delete(self, request, *args, **kwargs):
        if not Comment.objects.filter(member__pk=request.user.id).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.destroy(request, args, kwargs)