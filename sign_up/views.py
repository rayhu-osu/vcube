from django.shortcuts import render
from .forms import ConsumerForm, StoreForm, LoginForm
from django.http import HttpResponseRedirect

def register(request):
    return render(request, 'sign_up/register.html')

def login(request):
    if request.method == 'POST':
        aForm = LoginForm(request.POST)
        redirect_address = ''
        if aForm.is_valid():
            if aForm.cleaned_data.get('user_type') == 'VIP':
                redirect_address = '/vip/'
            elif aForm.cleaned_data.get('user_type') == 'Vendor':
                redirect_address = '/vendor/'
            else:
                redirect_address = '/valet/3' # 3 is the driver_id, should change to variable later

            return HttpResponseRedirect(redirect_address)
    else:
        aForm = LoginForm()

    return render(request, 'sign_up/login.html', {'form': aForm})

def consumer (request):
    form = ConsumerForm()
    return render(request, 'sign_up/signup_consumer.html', {'form': form})      

def store (request):
    form = StoreForm()
    return render(request, 'sign_up/signup_store.html', {'form': form})      

def driver (request):
    form = ConsumerForm()
    return render(request, 'sign_up/signup_consumer.html', {'form': form})      

def success(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        aForm = ConsumerForm(request.POST)
        # check whether it's valid:
        if aForm.is_valid():

            # save in Consumer model
            aForm.save()

            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form

    else:
        aForm = ConsumerForm()

    return render(request, 'sign_up/register.html', {'form': aForm})

def thanks (request):

    return render(request, 'sign_up/thanks.html')