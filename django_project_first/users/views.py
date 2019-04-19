from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm  # to use for creating default user registration form
from django.shortcuts import redirect  # to be able to redirect to other pages after command
from django.contrib import messages  # messages.debug, messages.info, messages.success
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':  # we check to see if POST method are bring used
        form = UserRegistrationForm(request.POST)  # if POST then we must verify the request
        if form.is_valid():  # if validation is success
            form.save()  # to save the form into the database
            username = form.cleaned_data.get('username')  # get the validated data
            messages.success(request, 'Accounts created {}'.format(username))
            return redirect('blog-home_page')
    else:
        form = UserRegistrationForm()  # if not POST then nothing to verify

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
