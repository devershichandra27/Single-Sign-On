from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm, SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserFormView(View):
    form_class = UserForm
    template_name = 'chat/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, dict(form=form))


    #process filled data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password', '')
            user.set_password(password)
            user.save()
            return HttpResponse('Registration Successful! :-) <a href = "signin"> Click here to continue! </a> ')

        else:
            return render(request, self.template_name, dict(form=form))


class SignIn(View):
    form_class = SignInForm
    template_name = 'chat/signin_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, dict(form=form))

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'chat/app1.html', {})
        else:
            return HttpResponse('Something went wrong <a href = ""> Try again!</a> ')

@login_required(login_url="/chat/signin/")
def app1(request):
    user1 = request.user
    return render(request, 'chat/app1.html', {'user':user1.username})


@login_required(login_url="/chat/signin/")
def app2(request):
    user1 = request.user
    return render(request, 'chat/app2.html', {'user':user1.username})

@login_required(login_url="/chat/signin/")
def logoutview(request):
    logout(request)
    return HttpResponse('Logout Successful! :-) <a href = "/chat/signin"> Click here to continue! </a> ')
