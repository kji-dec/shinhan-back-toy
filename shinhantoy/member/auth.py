from django.contrib.auth.hashers import check_password
from .models import Member


class MemberAuth:
    
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            return None

        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if check_password(password, member.password):
            if member.status == '일반':
                return member
        
        return None