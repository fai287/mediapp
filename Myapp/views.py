from django.shortcuts import render,redirect
from Myapp.models import Appointment,Contact # Make sure 'Appointment' is imported, not 'appointment'

from Myapp.forms  import AppointmentForm,ImageUploadForm
from Myapp.models import User,ImageModel


import json
import requests
import requests

from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from Myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from Myapp.models import Contact, Appointment, Member, ImageModel
from Myapp.forms import AppointmentForm, ImageUploadForm




# Create your views here.


def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).exists():
            # return redirect('/')  # Uncomment this line if you intend to redirect
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')


def service(request):
    return render(request,'service-details.html')

def  starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    return render(request,'doctors.html')


"""def service(request):
    return render(request, 'services.html')"""

def services(request):  # Renamed to services
    return render(request, 'services.html')


def contacts(request):
    return render(request, 'contacts.html')


def departments(request):
    return render(request, 'departments.html')

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
#from .models import appointment  # Import the appointment model

def appointment(request):
    if request.method == 'POST':
        # Retrieve POST data
        name = models.CharField(max_length=255)
        email = models.EmailField()
        phone = models.CharField(max_length=15)
        date = models.DateField()  # The field for the appointment date
        department = models.CharField(max_length=255)  # Optional: Adjust as needed
        doctor = models.CharField(max_length=255)  # Optional: Adjust as needed
        message = models.TextField(blank=True, null=True)

        # Save the appointment to the database
        Appointment.objects.create(  # Use 'Appointment' here, not 'appointment'
            name=name,
            email=email,
            phone=phone,
            date=appointment_datetime,
            department=department,
            doctor=doctor,
            message=message
        )

        # Redirect to the same page or a success page after saving
        return redirect('appointment')  # Replace 'appointment' with the name of your URL pattern if needed.

    # Handle the GET request by rendering the empty appointment form
    return render(request, 'appointment.html')


def show(request):
    # Retrieve all appointments from the database
    #fetching all the data from the database
    appointments = Appointment.objects.all()  # Use 'Appointment' here, not 'appointment'
    contacts = Contact.objects.all()
    #return render(request, 'show.html', {'appointments': appointments}, 'contacts': contacts)#this  method{'appointments': appointments} is called python dictionary and it is used to pass data from the view to the template.
     # Pass both appointments and contacts to the template
    return render(request, 'show.html', {
        'appointments': appointments,
        'contacts': contacts
    })


#deleting the data from the appointment table and the contact table
def delete(request, id):

    try:
        appoint = Appointment.objects.get(id=id)
        appoint.delete()
    except Appointment.DoesNotExist:
        pass  
   
    try:
        con = Contact.objects.get(id=id)
        con.delete()
    except Contact.DoesNotExist:
        pass  
    return redirect('show')  


##function to get the data from the contact  form and save it to the database
def contacts(request):
    if request.method == 'POST':
        # Retrieve the data from the form (POST request)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(name, email, subject, message)  

        # Save the data to the database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Redirect to the same page or a success page after saving
        return redirect('contacts')

    # Render the contact form
    return render(request, 'contacts.html')


def edit(request, id):
    # Retrieve the appointment with the given ID from the database
    appointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'appointment': appointment})


def update(request, id):
    updateinfo = Appointment.objects.get(id=id)

    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')

        #rn render(request, 'edit.html', {'appointment': updateinfo})


    else:
        return render(request, 'edit.html')
        #return render(request, 'edit.html', {'appointment': updateinfo})
        
        
        
def register(request):
    if request.method == 'POST':
        members = User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')
       


def login(request):
    return render(request,'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

#mpesa api functions {token,pay and stk}
def token(request):
    consumer_key = 'AGVONlZ7svqHcpJSEdeAimAbqWFXHl3Vqfc6iS7RddhhGXx6'
    consumer_secret = '7EGCI0ypkbNHiwEsgQpOEu123LNbxIBDrd1n1GTSRrizOFuzR2EdBez4Raci4tGh'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")











    


