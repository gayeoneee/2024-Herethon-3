from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, SubmitAnswer
from django.contrib.auth.decorators import login_required

# 스터디 홈 (현재 퀴즈 홈 - 목록 띄워줌)
@login_required
def quizHome(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizHome.html', {'quizzes': quizzes})

# 퀴즈의 질문
@login_required
def question(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'POST':
        selected_answer = int(request.POST['answer'])
        is_correct = (selected_answer == quiz.correct_answer)

        submit_answer, created = SubmitAnswer.objects.get_or_create(
            user=request.user,
            quiz=quiz,
            defaults={'answer': selected_answer, 'score': 0}
        )

        if not created:
            submit_answer.answer = selected_answer

        if is_correct:
            submit_answer.score = 1  # or whatever scoring logic you prefer

        submit_answer.save()

        return redirect('study:result', pk=pk)
    
    return render(request, 'questions.html', {'quiz': quiz})


@login_required
def result(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    submit_answer = get_object_or_404(SubmitAnswer, user=request.user, quiz=quiz)

    selected_answer = submit_answer.answer
    correct_answer = quiz.correct_answer
    is_correct = (selected_answer == correct_answer)
    
    return render(request, 'result.html', {
        'quiz': quiz,
        'selected_answer': selected_answer,
        'selected_answer_text': getattr(quiz, f'options{selected_answer}'),
        'correct_answer': correct_answer,
        'correct_answer_text': getattr(quiz, f'options{correct_answer}'),
        'is_correct': is_correct
    })


