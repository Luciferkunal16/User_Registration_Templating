
from django.shortcuts import redirect, render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, SignUpForm
from .models import UserDetail


def home_page(request):
    return render(request, 'user/home.html', {})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserDetail.objects.filter(username=user_name, password=password)
            if user:
                user_detail = UserDetail.objects.get(username=user_name, password=password)
                context = {"user_name": user_detail.username,
                           "full_name": user_detail.fullname,
                           "email": user_detail.fullname,
                           "age": user_detail.age
                           }
                return render(request, 'user/afterlogin.html', context=context)

    else:
        form = SignUpForm()
    return render(request, 'user/login.html', {'form': form})


@csrf_exempt
def registration(request):
    """
    this method is created for newuser registration
    :param request: passing the request
    :return: outcome result
    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            name = form.cleaned_data['fullname']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email_id']
            age = form.cleaned_data.get('age')
            form.save()
            print(user_name)

            return HttpResponse("succsessfull")

    else:
        form = SignUpForm()
    return render(request, 'user/registration.html', {'form': form})
