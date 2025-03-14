from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# working with form
from .forms import PropertyForm, WorkGen, Buildsec, Electsection, Civilsection
from .forms import ContractForm
from .models import UserProfile


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")  # Redirect to dashboard page
#         else:
#             messages.error(request, "Invalid username or password")
#
#     return render(request, "login.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('listReg')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'User not found')

    return render(request, 'login.html')

def listReg(request):
    return render(request, "list.html")





# def property_form(request):
#     if request.method == "POST":
#         form = PropertyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')  # Create a success page later
#     else:
#         form = PropertyForm()
#
#     return render(request, 'form1.html', {'form': form})


def property_form(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # ✅ Ensures data is saved properly
            return redirect('success1')  # Ensure 'success' is a valid URL name
    else:
        form = PropertyForm()
        print('nothing')

    return render(request, "form1.html", {"form": form})



def upload_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContractForm()

    return render(request, 'form2.html', {'form': form})




def upload_contractBuildsec(request):
    if request.method == 'POST':
        form = Buildsec(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = Buildsec()

    return render(request, 'buildingsection.html', {'form': form})


def upload_contractWorkGen(request):
    if request.method == 'POST':
        form = WorkGen(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = WorkGen()

    return render(request, 'workGeneral.html', {'form': form})








def upload_contractElectsection(request):
    if request.method == 'POST':
        form = Electsection(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = Electsection()

    return render(request, 'electricsection.html', {'form': form})







def upload_contractCivilsection(request):
    if request.method == 'POST':
        form = Civilsection(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = Civilsection()

    return render(request, 'civileng.html', {'form': form})






def lands_section_view(request):
    return render(request, 'landvault.html')


def success_view(request):
    return render(request, "success.html")

def success_view1(request):
    return render(request, "success1.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        # UserProfile.objects.create(user=user, phone=phone)

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')