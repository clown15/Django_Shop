from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import SignUpForm,SignInForm
from .models import User
# Create your views here.
def index(request):
    return render(request,"index.html", {'user':request.session.get('user')})

class SignUpView(FormView):
    template_name='signup.html'
    form_class = SignUpForm
    success_url = '/signin'

    def form_valid(self,form):
        user = User(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            level = 'user'
        )
        user.save()
        
        return super().form_valid(form)

class SignInView(FormView):
    template_name = 'signin.html'
    form_class = SignInForm
    success_url = '/'

    def form_valid(self,form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)