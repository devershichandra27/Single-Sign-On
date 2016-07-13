from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import View
from .models import Message
from .forms import UserForm, SignInForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.




class MessageCreate(CreateView):
    model = Message
    fields = ['Sender', 'Recipient', 'Mails']


'''@login_required(login_url='/chat/signin')
def inboxview1(request):
    template_name = 'chat/inbox.html'
    all_messages = Message.objects.filter(Sender='Deadpool')

    return render(request, template_name, {'all_messages':all_messages, 'user':user})'''



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
            all_messages = Message.objects.filter(Sender=str(user).title())
            context = dict(user=user, all_messages=all_messages)
            return render(request, 'chat/inbox.html', context)
        else:
            return HttpResponse('Something went wrong <a href = ""> Try again!</a> ')
