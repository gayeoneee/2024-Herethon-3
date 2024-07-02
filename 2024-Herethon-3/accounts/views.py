from django.shortcuts import render, redirect
from .models import CustomUsers
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 임시페이지
def temp(request):
    return render(request, 'temp.html')

def logoutTemp(request):
    return render(request, 'logout.html')

""" 이메일 인증 -> 이메일 중복으로 대체 """
# 이메일 인증 (중복 확인)
@csrf_exempt  # 필요 시 CSRF 검사 비활성화
def check_email(request):
    email = request.POST.get('email')
    if CustomUsers.objects.filter(email=email).exists():
        return JsonResponse({'is_taken': True})
    else:
        return JsonResponse({'is_taken': False})

# 회원가입 
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
    
# 로그인 
def login(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        password = request.POST['password']
        user = authenticate(request, username=userId, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('accounts:temp')
        else:
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('accounts:logoutTemp')
