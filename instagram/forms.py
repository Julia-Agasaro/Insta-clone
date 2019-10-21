from django import forms
from .models import Profile,Image,Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['likes','profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'comment_owner']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')
        exclude = ['user']
