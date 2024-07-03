from django.contrib import admin
from .models import Quiz, SubmitAnswer, FlashCard, SavedFlashCard

""" 퀴즈"""
# 퀴즈 
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question', 'options1', 'options2', 'options3', 'options4', 'correct_answer')
    search_fields = ('title', 'question')
    list_filter = ('title',)

# 사용자 퀴즈 정답 
@admin.register(SubmitAnswer)
class SubmitAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'answer', 'score')
    search_fields = ('user__username', 'quiz__title', 'answer')
    list_filter = ('score',)


""" 플래시 카드 """
# 플래시 카드
@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject')
    search_fields = ('subject',)
    list_filter = ('subject',)


# 사용자 저장 플래시 카드
@admin.register(SavedFlashCard)
class SavedFlashCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'flashcard')
    search_fields = ('user__username', 'flashcard__subject')
    list_filter = ('user',)