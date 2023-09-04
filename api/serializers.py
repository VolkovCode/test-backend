from rest_framework import serializers
from question.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):

    # answers  = serializers.
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    question_answer = AnswerSerializer(many=True)
    
    class Meta:
        model = Question
        # fields = '__all__'
        fields = ('id', 'question', 'question_answer')
    

