import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import app_user
from .models import UserDetails
from django.forms.models import  model_to_dict


def welcome_page(request):
    UserDetails.objects.all().delete()
    return render(request, 'Welcome_page.html')


def test(request):
    return HttpResponse(
        json.dumps('successful'),
        content_type="application/json"
    )


def home_page(request):
    return render(request, 'home_page.html')


def input_click_evnt(request):
    UserDetails.objects.all().delete()
    json_data = json.loads(request.body)
    new_user_data = UserDetails(
        first_name= json_data['first_name'],
        last_name =json_data['last_name'],
        phone_number=json_data['phone_number']
    )
    new_user_data.save()
    u = UserDetails.objects.all().first()
    return render(request, 'Log-in.html', {'form': app_user()})


def user_details_view(request):
    if UserDetails.objects.all().count()>0:   # restore data
        user_details = UserDetails.objects.all().first()
        form = app_user(model_to_dict(user_details))
        return render(request, 'Log-in.html', {'form': form})
    else:  # new session
        if request.method == 'POST':
            form = app_user(request.POST or None)
            return render(request, 'Log-in.html', {'form':form})



