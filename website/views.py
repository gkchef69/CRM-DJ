from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm


def home(request):
	# records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Έχετε συνδεθεί!")
			return redirect('home')
		else:
			messages.success(request, "Παρουσιάστηκε σφάλμα κατά τη σύνδεση, δοκιμάστε ξανά...")
			return redirect('home')
	else:
		return render(request, 'home.html', {})



# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Εχετε αποσυνδεθεί...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "Έχετε εγγραφεί με επιτυχία! Καλως ήρθατε!")
            return redirect('home')
    else:
        form = SingUpForm()
        return render(request, 'register.html', {'form':form})
        
            
    return render(request, 'register.html', {'form':form})
