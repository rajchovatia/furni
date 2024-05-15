from django.shortcuts import render,redirect
from django.contrib import messages
from Authentication.models import User
from Service.hashing import custom_hasher
# Create your views here.


def RegisterView(request):
    if request.method == "POST":
        # Retrieving form data
        profile_image = request.FILES.get('profile_image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validating form data
        if not (first_name and last_name and email and password):
            messages.error(request, 'All fields are required.', extra_tags='danger')
            return render(request, "accounts/register.html")
        
        # Checking if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered.', extra_tags='warning')
            return render(request, "accounts/register.html")
        
        # Checking password length
        if len(password) < 8:
            messages.warning(request, 'Password must be at least 8 characters long.', extra_tags='warning')
            return redirect('signup')  # Assuming 'signup' is the name of the registration URL
        
        # Creating user object
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            profile_image=profile_image  # Assuming you have profile image field in your User model
        )
        # Hashing the password
        user.password = custom_hasher(password)
        user.save()
        
        # Sending success message and redirecting to login page
        messages.success(request, 'User Created Successfully.', extra_tags='success')
        return redirect('login')
    
    return render(request, "accounts/register.html")


def LoginView(request) :
    try :
        if request.method == "POST" :
            print("Current Inbuild User is ::->",request.user)
            email = request.POST.get('email')
            password = request.POST.get('password')
            # Validating form data
            if not (email and password):
                messages.error(request, 'Email and Password are required.', extra_tags='danger')
                return render(request, "accounts/login.html")
            
            # Fetching user by email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'This email does not exist.', extra_tags='danger')
                return redirect('login')
            if user.password == custom_hasher(password) :
                messages.success(request, 'Login Successfully !', extra_tags='success')
                return redirect('home')
            else :
                messages.error(request, 'Invalid password.', extra_tags='danger')
                return render(request, "accounts/login.html")
            
    except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}', extra_tags='danger')
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")





