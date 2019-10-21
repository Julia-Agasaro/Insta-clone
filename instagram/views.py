from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Image, Profile,Comment,Likes
from .forms import ProfileForm,ImageForm,CommentForm,ProfileEditForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all()
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

	
	

	return render(request,'profile/profile.html',locals())
@login_required(login_url='accounts/login/')
def edit(request):
     current_user = request.user

     if request.method == 'POST':
        if Profile.objects.filter(user_id= current_user):

            profile_form = ProfileEditForm(request.POST,request.FILES,instance = Profile.objects.get(user_id=current_user))
        else:
            profile_form = ProfileEditForm(request.POST,request.FILES)

        if profile_form.is_valid():
            userProfile=profile_form.save(commit = False)
            userProfile.user = current_user
            userProfile.save()
            
       
           
     else:

        profile_form = ProfileEditForm()
        return render(request, 'profile/profileForm.html', locals())


@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'upload.html',locals())

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return redirect('home')

def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect(home)

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())


@login_required(login_url='/accounts/login/')
def search_results(request):
    if request.POST.get['search']:
        search_term = request.GET.get("search")
        profiles = Profile.objects.filter(user__username__icontains = search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"profiles":profiles})
    else:
        message = "You haven't searched for any item"
        return render(request,'search.html',{"message":message})   