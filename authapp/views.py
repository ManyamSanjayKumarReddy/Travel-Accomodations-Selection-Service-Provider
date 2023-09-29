from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from authapp.models import UserProfile
from ecommerceapp.models import Orders, OrderUpdate, Rating
from django.core.exceptions import ObjectDoesNotExist


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        state = request.POST['state']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request, "Email is Taken")
                return render(request, 'signup.html')
        except User.DoesNotExist:
            pass

        user = User.objects.create_user(email, email, password)
        user.save()

        UserProfile.objects.create(user=user, name=name, phone_number=phone_number, city=city, state=state)

        messages.success(request, "Registration Successful")
        return redirect('/auth/login/')
    
    return render(request, "signup.html")


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

        order_updates = {}
        for order in user_orders:
            updates = OrderUpdate.objects.filter(order_id=order.order_id)
            order_updates[order] = updates

        user_ratings = Rating.objects.filter(user=request.user)

        context = {
            'user_profile': user_profile,
            'user_orders': user_orders,
            'order_updates': order_updates,
            'user_ratings': user_ratings,
        }

        return render(request, 'profile.html', context)
    else:
        return render(request, 'login.html')
