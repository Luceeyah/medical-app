from django.shortcuts import render, redirect
from .models import User, Appointment, MedicalRecord
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import MedicalRecordForm
from django.core.mail import send_mail
from django.contrib import messages
from django.template import loader
# Create your views here.

# Get Counts


def FirstPage(request):
    return render(request, 'users/home.html', {})


def appointment_approval(request):

    total_count = Appointment.objects.all().count()
    approved_count = Appointment.objects.filter(approved=True).count()
    print(total_count)

    Ans = request.user.email

    # appointments = Appointment.objects.filter(doc_email=me)
    appointments = Appointment.objects.all()
    if request.user.is_physician:
        if request.method == "POST":

            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')

            # Uncheck all events
            appointments.update(approved=False)

            # Update the database
            for x in id_list:
                Appointment.objects.filter(pk=int(x)).update(approved=True)

            # Show Success Message and Redirect
            messages.success(
                request, ("Event List Approval Has Been Updated!"))
            return redirect('appointment-approval')
        else:
            return render(request, 'users/appointment_approval.html', {'appointments': appointments, 'total_count': total_count, 'approved_count': approved_count})
    else:
        messages.success(request, ("You aren't authorized to view this page!"))
        # return redirect('home-page')

    return render(request, 'users/appointment_approval.html')


@login_required(login_url='/login')
def appointment(request):

    # print(request.user)
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_schedule = request.POST['your-schedule']
        your_message = request.POST['your-message']
        doc_email = request.POST['doc-email']

        # save the new appointment
        new_appointment = Appointment.objects.create(
            name=your_name, phone_no=your_phone, email=your_email, schedule_date=your_schedule, message=your_message, doc_email=doc_email)

        new_appointment.save()

        # send an email
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + \
            your_email + " Schedule: " + your_schedule + " Message: " + your_message

        send_mail(
            'Appointment Request',  # subject
            appointment,  # message
            your_email,  # from email
            [doc_email],  # To Email
        )

        return render(request, 'users/appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_schedule': your_schedule,
            'your_message': your_message
        })
    else:
        return render(request, 'users/home.html', {})


def show_doc(request, doc_id):
    doctor = User.objects.get(pk=doc_id)
    user = request.user
    return render(request, 'users/show_doc.html', {'doctor': doctor, 'user': user})


def search_doc(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doctors = User.objects.filter(is_physician=True)
        return render(request, 'users/search_doc.html', {'searched': searched,
                                                         'doctors': doctors})
    else:
        return render(request, 'users/search_doc.html', {})


@login_required
def HomePage(request):
    profile = request.user.first_name
    if request.user.is_physician == False:
        tmp = 'users/base.html'
    else:
        tmp = 'users/base2.html'
    context = {
        'profile': profile,
        'tmp': tmp,
    }
    return render(request, 'users/index.html', context)




def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('phone')

        new_user = User.objects.create_user(
            first_name=fname, last_name=lname, email=email, mobile=mobile, password=password)

        new_user.save()
        return redirect('login-page')
    return render(request, 'users/register.html', {})


def RegisterDoc(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('phone')

        new_user = User.objects.create_user(
            first_name=fname, last_name=lname, email=email, mobile=mobile, password=password, is_physician=True)

        new_user.save()
        return redirect('login-page')
    return render(request, 'users/registerMed.html', {})


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'users/login.html', {})


def add_profile(request):
    submitted = False
    if request.method == "POST":
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.patient = request.user
            # profile.date_of_diagnosis = form.cleaned_data['date_of_diagnosis']
            profile.save()
            submitted = True

            render(request, 'users/profile.html',
                   {'form': form, 'submitted': submitted})
    else:
        form = MedicalRecordForm()
        
    return render(request, 'users/profile.html', {'form': form, 'submitted': submitted})


def chart(request):
    users = MedicalRecord.objects.all()
    num_users=len(users)
    items =[0,0,0,0,0]
    for i in range(num_users):
        if users[i].stomach_ache == "YES":
            items[0] += 1
        if users[i].malaria== "YES":
            items[1] += 1
        if users[i].injuries == "YES":
            items[2] += 1
        if users[i].head_ache == "YES":
            items[3] += 1
        if users[i].cough == "YES":
            items[4] += 1
        if users[i].fever== "YES":
            items[5] += 1
        

    labels = ['Stomach_ache', 'Malaria', 'Injuries', 'Headache', 'Cough', 'Fever', ]
    data = {
            "labels": labels,
            "items": items
    }
    return render(request, "users/chart.html", {"data": data})

    return JsonResponse(data)

    
      
    


def table(request):
    user_list = MedicalRecord.objects.all()
    return render(request, "users/table.html", {"users": user_list})


# Create your views here.
