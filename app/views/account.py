from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import redirect


def create_account_page(request):
    template = loader.get_template('app/create_account.html')
    context = {
        "var":1
    }
    return HttpResponse(template.render(context, request))

def create_account(request):
    user = User.objects.create_user(username=request.POST["username"],
                                     email=request.POST["email"],
                                     password=request.POST["password"])
    user.save()
    return redirect("/app")
