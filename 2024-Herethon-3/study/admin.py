# study/admin.py
from django.contrib import admin
from .models import Quiz, SubmitAnswer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question', 'options1', 'options2', 'options3', 'options4', 'correct_answer')
    search_fields = ('title', 'question')
    list_filter = ('title',)

@admin.register(SubmitAnswer)
class SubmitAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'answer', 'score')
    search_fields = ('user__username', 'quiz__title', 'answer')
    list_filter = ('score',)
