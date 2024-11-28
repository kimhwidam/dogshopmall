# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth import logout
# from .forms import CustomUserCreationForm


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'user/signup.html', {'form': form})




# import logging

# if __name__ == '__main__':
#     # 모듈이 직접 실행될 때 실행할 코드
#     logger = logging.getLogger(__name)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 회원가입 성공 후 리디렉션

    else:
        form = CustomUserCreationForm()

    # 유효성 검사 실패 시, 폼과 오류 메시지를 함께 전달
    context = {'form': form}
    return render(request, 'user/registration.html', context)


