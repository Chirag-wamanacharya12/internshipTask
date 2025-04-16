from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import datetime
from .models import User
from django.contrib.auth import get_user_model

# Create your views here.

def loginview(request):
    return render(request, 'login.html')

@login_required
def admindash(request):
    user = User.objects.all()
    request.session['last_activity']=str(datetime.datetime.now())
    request.session.set_expiry(10)
    request.session['email'] = request.user.email
    logout(request)  # Logs out the current user
    context = {'users':user}
    return render(request, 'user/admin.html',context)

def register(request):
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            
            # Set session data
            request.session['email'] = email
            request.session['user_id'] = user.id
            request.session['last_activity'] = str(datetime.datetime.now())
            
            # Optional: Session expires in 10 minutes
            request.session.set_expiry(60)  # 60 seconds = 1 minutes
            
            return redirect('adminDash')  # Redirect after login
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'login.html')

def logoutView(request):
    logout(request)  # Logs out the current user
    return redirect('login')

def loginpage(request):
    userID = request.user.id
    user = User.objects.filter(id=userID).first()
    context = {'user':user}
    return render(request, 'loginSuccess.html',context)




User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        # Check for duplicates
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        user = User.objects.create(
            full_name=full_name,
            username=username,
            email=email,
            user_type=user_type,
        )

        user.set_password(password)

        # Check if user is admin and set is_staff or is_superuser if needed
        if user_type == 'admin':
            user.is_staff = True
            user.is_superuser = True

        user.save()
        login(request, user)
        if user_type == 'admin':
            return redirect('adminDash')  # admin dashboard URL name
        else:
            return redirect('loginSuccess')  # user dashboard URL name

    return render(request, 'register.html')

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    try:
        user.delete()
        messages.success(request, f"User '{user.full_name}' deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting user: {e}")
    
    return redirect('adminDash')  # Make sure this matches your URL pattern name
