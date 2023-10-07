from django.shortcuts import render, redirect
from .models import Participant, Test
from .forms import RegisterForm, LoginForm, AddTestForm
from django.contrib.auth.hashers import make_password, check_password
from .decorators import user_login_required


# Create your views here.

def register(request):
    form = RegisterForm()
    success = None

    if request.method == 'GET':
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():  # Check if the form is valid
            cleaned_data = form.cleaned_data
            if Participant.objects.filter(username=cleaned_data['username']).exists():
                error = "This username is already taken"
                return render(request, 'register.html', {'form': form, 'error': error})

            if Participant.objects.filter(email=cleaned_data['email']).exists():
                error = "This email is already taken"
                return render(request, 'register.html', {'form': form, 'error': error})

            cleaned_data['password'] = make_password(cleaned_data['password'])
            new_user = Participant(**cleaned_data)
            new_user.save()
            success = "User created successfully"
        else:
            error = "Some error occured"
            return render(request, 'register.html', {'form': form, 'error': error})
            

    return render(request, 'register.html', {'form': form, 'success': success})

def login(request):
    form = LoginForm()

    if request.method == 'GET':
        return render(request, 'login.html', { 'form': form })

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user_data = (Participant.objects.get(username=username)).as_dict()
        
        if(check_password(password, user_data['password'])):
            print('Login Successfull !!')
            request.session['user_id'] = user_data['id']
            print(request.session)
            return redirect('time_sync:home')

        return render(request, 'login.html', {'form': form})
            
def get_user(request):
    return Participant.objects.get(id=request.session['user_id'])


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id'] # delete user session
    return redirect('time_sync:login')

@user_login_required
def home(request):

    if request.method == 'GET':
        if 'user_id' in request.session:
            user = get_user(request)
            return render(request, 'home.html', {'user': user})
        else:
            return redirect('time_sync:login')

@user_login_required
def add_test(request):
    success = None

    if request.method == 'GET':
        form = AddTestForm()
        return render(request, 'addTest.html', {'form': form})
    
    if request.method == 'POST':
        form = AddTestForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = form.save(commit=False)

            if (Test.objects.filter(test_name=cleaned_data['test_name'])).exists():
                error = "This test is already there"
                return render(request, 'addTest.html', {'form': form, 'error': error})
            
            user.save()
            success = "Test successfuly added"
        else:
            error = "Some error occured"
            return render(request, 'addTest.html', {'form': form, 'error': error})
        
    return render(request, 'addTest.html',  {'form': form, 'success': success})
        
            
            
        

