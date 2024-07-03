from django.urls import path
from .views import studyHome, quizHome, question, result
from .views import flashCardHome, flashCardSubject, flashCardContent, saveFlashCard

app_name = 'study'

urlpatterns = [
    # study home
    path('', studyHome, name='studyHome'),

    # quiz
    path('quiz/', quizHome, name='quizHome'),  # quiz 임시 홈 (quiz 목록)
    path('question/<int:pk>/', question, name='question'),  # Quiz question page
    path('result/<int:pk>/', result, name='result'),  # Result page

    # flash card
    path('flashcards/', flashCardHome, name='flashCardHome'),  # Flash card 임시 홈(목록)
    path('flashcard/<int:pk>/', flashCardSubject, name='flashCardSubject'),  # Flash card subject page
    path('flashcard/<int:pk>/content/', flashCardContent, name='flashCardContent'),  # Flash card content page
    path('flashcard/<int:pk>/save/', saveFlashCard, name='saveFlashCard'),  # Save flash card
]