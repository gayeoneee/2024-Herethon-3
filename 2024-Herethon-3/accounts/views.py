from django.shortcuts import render, redirect
from .models import CustomUsers
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def temp(request):
    return render(request, 'temp.html')

def logoutTemp(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:temp')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        password = request.POST['password']
        user = authenticate(request, username=userId, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('accounts:temp')
        else: 
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."  # 에러 메시지 설정
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('accounts:logoutTemp')  # 올바른 URL 패턴 이름 전달


