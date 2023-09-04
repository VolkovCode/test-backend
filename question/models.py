from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=500, null=False)
    
    def __str__(self):
        return self.question
    
class Answer(models.Model):
    answer = models.CharField(max_length=300, null=False)
    is_right = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answer')

    def __str__(self):
        return self.answer
    