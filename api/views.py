from rest_framework import viewsets
from .serializers import QuestionSerializer
from question.models import Question, Answer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    question = Answer.objects.filter(question=Question.objects.get(id=1))
    # def get_queryset(self):
    #     queryset = Answer.objects.filter(question=Question.objects.get(id=1))
    #     return queryset
