from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Profile

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')     


class Register(View):

    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):

        form = UserCreationForm(request.POST)
        picture = request.POST['picture']
        nickname = request.POST['nickname']
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user, picture=picture, nickname=nickname)
            # Authentication should always be done before login....
            # In this case, we just created the user successfully, so obviously the authenticate will work.
            user = authenticate(form.cleaned_data['username'], form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')

        return redirect('register')