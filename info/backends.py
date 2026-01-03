from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student, Teacher

User = get_user_model()


class NameAuthBackend(ModelBackend):
    """
    Custom authentication backend that allows login using Student.name or Teacher.name
    Falls back to username if name lookup fails.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('username')
        
        if username is None or password is None:
            return None
        
        # First, try to find by Student name
        try:
            student = Student.objects.get(name__iexact=username)
            if student.user and student.user.check_password(password):
                return student.user
        except Student.DoesNotExist:
            pass
        
        # Then, try to find by Teacher name
        try:
            teacher = Teacher.objects.get(name__iexact=username)
            if teacher.user and teacher.user.check_password(password):
                return teacher.user
        except Teacher.DoesNotExist:
            pass
        
        # Fall back to default username authentication
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


