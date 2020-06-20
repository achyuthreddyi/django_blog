from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'dear {username}! your account has been created you can bloody login')
            return redirect('login')           


    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'title':'Signup','form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

# messages for
# debug success warning error info 