from django.conf.urls import url
from .views import StudentView

urlpatterns = [
    url(
        r'students/?$',
        StudentView.as_view({
            'post': 'create',
            'get': 'list'
        }),
        name='student_list'
    ),
    url(
        r'students/(?P<student_id>[0-9]+)/?$',
        StudentView.as_view({
            'get': 'retrieve',
            'patch': 'partial_update'
        }),
        name='student_detail'
    )
]
