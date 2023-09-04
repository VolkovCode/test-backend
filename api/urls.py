from rest_framework import routers
from .views import QuestionViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'api')))
]
