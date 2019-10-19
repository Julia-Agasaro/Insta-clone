from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile
from .forms import ProfileForm,ImageForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    profile = Profile.objects.all()
    return render(request,'home.html',locals())

    
@login_required(login_url='/accounts/login/')
def profile(request,prof_id):
	'''
	Method that fetches a users profile page
	'''
	user=User.objects.get(pk=prof_id)
	images = Image.objects.filter(profile = prof_id)
	title = User.objects.get(pk = prof_id).username
	profile = Profile.objects.filter(user = prof_id)

	
	

	return render(request,'profile/profile.html',{"images":images,"profile":profile,"title":title})
	

