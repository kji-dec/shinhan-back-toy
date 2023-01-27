from rest_framework import serializers

from .models import Order, Comment, Like


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.like_set.all().count()

    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )
    
    class Meta:
        model = Like
        fields = '__all__'