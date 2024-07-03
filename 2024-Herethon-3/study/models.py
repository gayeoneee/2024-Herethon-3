from django.db import models
from django.conf import settings

# 퀴즈
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    options1 = models.CharField(max_length=100)
    options2 = models.CharField(max_length=100)
    options3 = models.CharField(max_length=100)
    options4 = models.CharField(max_length=100)
    correct_answer = models.IntegerField()  # 정답의 번호

    def __str__(self):
        return self.title

# 각각의 퀴즈를 푼 사용자의 답 저장
class SubmitAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to user
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # Link to quiz
    answer = models.IntegerField(null=True, blank=True)  # Store the user's selected answer
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"

    class Meta:
        ordering = ['score', 'user']
        unique_together = ('user', 'quiz')  # 사용자가 퀴즈당 하나의 답변만 가질 수 있는지 확인해야함