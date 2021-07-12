from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import SignUpForm,SignInForm

# Create your views here.

def index(request):
    return render(request, 'index.html',{'email':request.session.get('user')})

def SignOut(request):
    if "user" in request.session:
        del(request.session['user'])

    return redirect('/')


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = "/signin"

class SignInView(FormView):
    template_name = 'signin.html'
    form_class = SignInForm
    success_url = "/"

    # form유효성 검사끝난후 실행
    def form_valid(self,form):
        self.request.session['user'] = form.email
        return super().form_valid(form)