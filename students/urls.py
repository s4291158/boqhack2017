from django.conf.urls import url
from .views import StudentView

urlpatterns = [
    url(r'students/', StudentView.as_view({
        'post': 'create',
        'get': 'list'
    }))
]
