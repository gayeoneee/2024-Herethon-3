from django.urls import path
from .views import quizHome, question, result

app_name = 'study'

urlpatterns = [
    path('quiz/', quizHome, name='quizHome'),  # Home page showing quizzes
    path('question/<int:pk>/', question, name='question'),  # Quiz question page
    path('result/<int:pk>/', result, name='result'),  # Result page
]