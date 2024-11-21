from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Patient
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.
# Homepage view
def index(request):
    return render(request, 'index.html')

# Sign up view



def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')  # Correct redirect usage
            elif User.objects.filter(username=username).exists():  # User uses `username` instead of `username`
                messages.info(request, 'Name has been used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'Passwords do not match')  # Inform user of password mismatch
            return redirect('signup')

    else:  # Handle GET requests
        return render(request, 'signup.html')  # Render the signup form
        
# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']  # Changed from 'username' to 'username'
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials not found')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

# CRUD
@login_required
def dashboard(request):
    patient_records= Patient.objects.all()

    context = {'patients': patient_records}
    print(patient_records)  # Debugging
    return render(request, 'dashboard.html', context=context)

def register(request):
    if request.method == "POST":
        patient_id = request.POST.get("patientId")
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        disease_category = request.POST.get("diseaseCategory")
        nature = request.POST.get("nature")
        address = request.POST.get("address")

        try:
            # Save patient data to the database
            patient = Patient.objects.create(
                patient_id=patient_id,
                name=name,
                age=age,
                gender=gender,
                phone=phone,
                email=email,
                disease_category=disease_category,
                nature=nature,
                address=address
            )
            messages.success(request, "Patient registered successfully!")
            return redirect('dashboard')  # Redirect to dashboard after successful registration
        except Exception as e:
            messages.error(request, f"Error registering patient: {str(e)}")
    
    return render(request, 'register.html')


def update(request, pk):
    # fetch the patient details using primary key (pk)
    patient = get_object_or_404(Patient, pk=pk)
    if request.method =='POST':
        # Update the patient record with the submitted data
        patient.patient_id = request.POST.get('patientId')
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.disease_category = request.POST.get('diseaseCategory')
        patient.nature = request.POST.get('nature')
        patient.address = request.POST.get('address')
        patient.save()

        # Redirect to the dashboard or a success page
        return redirect('dashboard')


    return render(request, 'update.html', {'patient': patient})

@login_required
def read(request, pk):
    patient= get_object_or_404(Patient, id=pk)
    return render(request, 'read.html', {'patient': patient})

def delete(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient record deleted successfully.')
        return redirect('dashboard')
    return render(request, 'delete.html', {'patient': patient})


def features(request):
    return render(request, 'features.html')


def chart(request):
    # Robust data collection with error checking
    try:
        # Get total patient count
        total_patients = Patient.objects.count()
        
        # Disease Category Distribution
        category_disease_data = list(
            Patient.objects.values('disease_category')
            .annotate(count=Count('disease_category'))
            .order_by('-count')
        )
        
        # Nature Distribution
        nature_data = list(
            Patient.objects.values('nature')
            .annotate(count=Count('nature'))
            .order_by('-count')
        )
        
        # Gender and Disease Category Distribution
        gender_disease_data = list(
            Patient.objects.values('gender', 'disease_category')
            .annotate(count=Count('id'))
            .order_by('disease_category', 'gender')
        )
        
        # Debugging print
        print(f"Total Patients: {total_patients}")
        print(f"Category Data: {category_disease_data}")
        print(f"Nature Data: {nature_data}")
        print(f"Gender Disease Data: {gender_disease_data}")
        
        # Prepare context for template
        context = {
            'total_patients': total_patients,
            'category_disease_data': category_disease_data,
            'nature_data': nature_data,
            'gender_disease_data': gender_disease_data
        }
        
        return render(request, 'chart.html', context)
    
    except Exception as e:
        # Log any unexpected errors
        print(f"Error in chart view: {e}")
        return render(request, 'chart.html', {'error': str(e)})
