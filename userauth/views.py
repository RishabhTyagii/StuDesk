from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignUpForm
from .utils import generate_otp, send_otp_email
from django.contrib import messages
from quantum.views import indexpage
from .models import Profile

from notes.models import BTechNotes, MBANotes, MCANotes
from quantum.models import BTechQuantum,MBAQuantum,MCAQuantum
from exam_papers.models import BTechExamPapers, MBAExamPapers, MCAExamPapers 
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user:
                login(request, user)
                # Redirect to 'index' after successful login
                return redirect('index')  # Update this line to redirect to your index page
    else:
        form = LoginForm()
    return render(request, 'userauth/login.html', {'form': form})

@login_required
def user_profile(request):
    profile = request.user.profile
    return render(request, 'userauth/profile.html', {'profile': profile})



# Store OTP temporarily (you can use sessions or database)
otp_storage = {}

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = generate_otp()
            otp_storage[email] = otp
            send_otp_email(email, otp)
            request.session['pending_user'] = form.cleaned_data
            return redirect('verify_otp')
    else:
        form = SignUpForm()
    return render(request, 'userauth/signup.html', {'form': form})


# views.py (continued)
def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('pending_user', {}).get('email')
        entered_otp = request.POST.get('otp')

        if email and entered_otp == otp_storage.get(email):
            # Save user to DB using the form
            user_data = request.session.pop('pending_user')
            form = SignUpForm(user_data)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'userauth/verify_otp.html')


def user_logout(request):
    logout(request)  # This will log out the user
    return redirect('index') 

def index(request): 
    BTechQuantum1=BTechQuantum.objects.all()
    MBAQuantum1=MBAQuantum.objects.all()
    MCAQuantum1=MCAQuantum.objects.all()
    BTechNotes1=BTechNotes.objects.all()
    MBANotes1=MBANotes.objects.all()
    MCANotes1=MCANotes.objects.all()
    BTechExam_paper=BTechExamPapers.objects.all()
    MBAExam_paper=MBAExamPapers.objects.all()
    MCAExam_paper1=MCAExamPapers.objects.all()


    return render(request,'index.html',{'BTechQuantum1':BTechQuantum1,'MBAQuantum1':MBAQuantum1,'MCAQuantum1': MCAQuantum1,'BTechNotes1':BTechNotes1,'MBANotes1':MBANotes1,'MCANotes1': MCANotes1,'BTechExam_paper':BTechExam_paper,'MBAExam_paper':MBAExam_paper,'MCAExam_paper1': MCAExam_paper1}) 
    