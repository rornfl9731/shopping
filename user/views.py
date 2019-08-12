from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import Suser


# Create your views here.


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')});


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    # 폼에 있던 유효성 검사를 뷰로 옮김
    def form_valid(self, form):
        user = Suser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 유효성검사가 끝나고 로그인이 되었을때 세션에 등록
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del (request.session['user'])
    return redirect('/')
