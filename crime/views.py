from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Crime, Bookmark
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CrimeForm, NewUserForm

@login_required
def create_crime(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            crime = form.save(commit=False)
            crime.reported_by = request.user
            crime.save()
            return redirect('crime_listing')
    else:
        form = CrimeForm()
    return render(request, 'create_crime.html', {'form': form})

@login_required
def bookmark_crime(request, crime_id):
    crime = Crime.objects.get(pk=crime_id)
    bookmark = Bookmark(user=request.user, crime=crime)
    bookmark.save()
    return redirect('bookmark_listing')

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("crime_listing")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("crime_listing")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def crime_listing(request):
    crimes = Crime.objects.all()
    return render(request, 'crime_listing.html', {'crimes': crimes})

@login_required
def bookmark_listing(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark_listing.html', {'bookmarks': bookmarks})
