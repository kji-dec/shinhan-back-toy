from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import (
    OrderSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeSerializer
)
from .models import Order, Comment, Like

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        ord_no = self.request.query_params.get('ord_no')

        if ord_no:
            orders = orders.filter(ord_no__contains=ord_no)
        
        return orders.order_by('id')

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
        return Comment.objects.filter(order_id=self.kwargs.get('order_id'))\
                    .select_related('member', 'order')\
                    .order_by('-id')
    
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
        if not Comment.objects.filter(member__pk=self.request.user.id, pk=self.kwargs.get('pk')).exists():
            return Comment.objects.none()
        return Comment.objects.all().order_by('id')
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

class LikeCreateView(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    
    def post(self, request, *args, **kwargs):
        like = Like.objects.filter(member=request.user.id, comment_id=kwargs.get('comment_id'))
        print(request.user.id, kwargs.get('comment_id'))
        if like.exists():
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return self.create(request, args, kwargs)