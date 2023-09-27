from django.shortcuts import render,redirect, get_object_or_404
from ecommerceapp.models import Contact,RoomType,OrderUpdate,Orders, Rating
from django.contrib import messages
from math import ceil
from ecommerceapp import keys
MERCHANT_KEY=keys.MK
from django.views.decorators.csrf import  csrf_exempt
from PayTm import Checksum
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from django.db.models import Avg
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.
def index(request):

    allRooms = []
    room_category = RoomType.objects.values('category','id')
    # print(room_category)
    categories = {item['category'] for item in room_category}
    for cat in categories:
        prod= RoomType.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allRooms.append([prod, range(1, nSlides), nSlides])

    params= {'allRooms':allRooms}

    return render(request,"index.html",params)

def room_detail(request, room_id):
    room = get_object_or_404(RoomType, id=room_id)
    return render(request, 'room_detail.html', {'room': room})
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we will get back to you soon..")
        return render(request,"contact.html")


    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")



def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="Room has been Confirmed")
        update.save()
        thank = True
# # PAYMENT INTEGRATION

        id = Order.order_id
        oid=str(id)+"ShopyCart"
        param_dict = {

            'MID':keys.MID,
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            a=response_dict['ORDERID']
            b=response_dict['TXNAMOUNT']
            rid=a.replace("ShopyCart","")
           
            print(rid)
            filter2= Orders.objects.filter(order_id=rid)
            print(filter2)
            print(a,b)
            for post1 in filter2:

                post1.oid=a
                post1.amountpaid=b
                post1.paymentstatus="PAID"
                post1.save()
            print("run agede function")
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    currentuser=request.user.username
    items=Orders.objects.filter(email=currentuser)
    rid=""
    for i in items:
        print(i.oid)
        # print(i.order_id)
        myid=i.oid
        rid=myid.replace("ShopyCart","")
        print(rid)
    # status=OrderUpdate.objects.filter(order_id=int(rid))
    # for j in status:
    #     print(j.update_desc)

   
    context ={"items":items}
    # print(currentuser)
    return render(request,"profile.html",context)


@login_required
def room_detail(request, room_id):
    room = get_object_or_404(RoomType, id=room_id)
    user_rating = Rating.objects.filter(room=room, user=request.user).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']

            if user_rating:
                user_rating.rating = rating
                user_rating.comment = comment
            else:
                user_rating = Rating.objects.create(
                    room=room,
                    user=request.user,
                    rating=rating,
                    comment=comment,
                )
            user_rating.save()
            return redirect('/')

    else:
        form = RatingForm()

    # Get all ratings for the room (excluding the user's own rating)
    ratings = Rating.objects.filter(room=room).exclude(user=request.user)

    # Calculate the average rating for the room
    average_rating = Rating.objects.filter(room=room).aggregate(Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST' and 'delete_rating' in request.POST:
        # Check if the user has a rating and delete it
        if user_rating:
            user_rating.delete()

            # Redirect to the same page after deleting the rating
            return redirect('room_detail', room_id=room_id)

    return render(request, 'room_detail.html', {'room': room, 'ratings': ratings, 'user_rating': user_rating, 'form': form, 'average_rating': average_rating})


def delete_booking(request, order_id):
    if request.method == 'POST':
        # Fetch the order based on order_id
        order = get_object_or_404(Orders, order_id=order_id)

        # Check if the order belongs to the current user (optional, for security)
        if order.email == request.user.email:
            # Delete the order
            order.delete()
            messages.success(request, 'Booking deleted successfully.')
        else:
            messages.error(request, 'You do not have permission to delete this booking.')

    return redirect('/auth/profile/')



# In your ecommerceapp/views.py

def update_appointment_date(request, order_id):
    if request.method == 'POST':
        # Fetch the order based on order_id
        order = get_object_or_404(Orders, order_id=order_id)

        # Check if the order belongs to the current user (optional, for security)
        if order.email == request.user.email:
            # Get the appointment date from the form
            appointment_date_str = request.POST.get('appointment_date')

            # Convert the date to the correct format (YYYY-MM-DD)
            try:
                appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
                order.appointment_date = appointment_date
                order.updated_appointment_date = appointment_date  # Update the updated_appointment_date field
                order.save()
                messages.success(request, 'Appointment date set successfully.')
            except ValueError:
                messages.error(request, 'Invalid date format. Please use YYYY-MM-DD format.')
        else:
            messages.error(request, 'You do not have permission to set the appointment date.')

    return redirect('/auth/profile/')
