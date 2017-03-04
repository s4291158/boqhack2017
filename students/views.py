from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_url_kwarg = 'student_id'
    lookup_field = 'id'
