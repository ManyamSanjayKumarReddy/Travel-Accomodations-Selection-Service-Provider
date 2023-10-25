from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from authapp.models import UserProfile
from ecommerceapp.models import Orders, Rating
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # Form data is valid, create the user and profile
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            age = form.cleaned_data['age']
            detailed_address = form.cleaned_data['detailed_address']
            id_proof = form.cleaned_data['id_proof']
            id_proof_upload = form.cleaned_data['id_proof_upload']
            country = form.cleaned_data['country']
            password = form.cleaned_data['pass1']

            # Check for existing email (this is also done in the form, but it doesn't hurt to check again)
            if User.objects.filter(username=email).exists():
                messages.error(request, "Email is already taken")
            else:
                # Create the User and UserProfile
                user = User.objects.create_user(email, email, password)
                user.save()
                profile = UserProfile.objects.create(user=user, name=name, phone_number=phone_number, city=city, state=state, age=age, detailed_address=detailed_address, id_proof=id_proof, id_proof_upload=id_proof_upload, country=country)

                # Log the user in and redirect
                login(request, user)
                messages.success(request, "Registration Successful")
                return redirect('/auth/login/')
    else:
        form = SignupForm()

    return render(request, "signup.html", {'form': form})


def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request,'login.html')  

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')


def user_profile_details(request):
    if request.user.is_authenticated:

        user_profile = UserProfile.objects.get(user=request.user)

        user_orders = Orders.objects.filter(email=request.user.email)

        user_ratings = Rating.objects.filter(user=request.user)

        context = {
            'user_profile': user_profile,
            'user_orders': user_orders,
            'user_ratings': user_ratings,
        }

        return render(request, 'profile.html', context)
    else:
        return render(request, 'login.html')
