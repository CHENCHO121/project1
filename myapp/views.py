from django.shortcuts import render,redirect
from .forms import CreateUserForm,UserForm,ProfileForm
from .forms import UserForm,ProfileForm
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def ProfileView(request):
    return render(request,'common/profile.html')
@login_required
def create_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile is created!')
            return redirect('profile')

        else:
            return render(request, 'common/create_profile.html', {'form': form})
    else:
        form = ProfileForm()
        return render(request, 'common/create_profile.html', {'form': form})


@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        user_form =UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request,'common/profile_update.html',context)




def home(request):
    count=User.objects.count()
    return render(request,'home.html',{'user':count})

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '')
        con=Contact(name=name,email=email,phone=phone,msg=msg)
        con.save()
    return render(request,'contact.html')

def Signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            u=form.cleaned_data.get('username')
            return redirect('login')
    return render(request,'registration/register.html',{'form':form})

# forgot_password



