from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_pic =models.ImageField(upload_to = 'media/')
    bio = models.CharField(max_length=255)
    user = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return str(self.bio)


    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_profile_by_username(cls, user):
        profiles = cls.objects.filter(user__contains=user)
        return profiles
class Image(models.Model):
    pic= models.ImageField(upload_to = 'media/')
    # pic=ImageField(manual_crop='1080x800', blank=True)
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    profile_details = models.ForeignKey(Profile)

    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images


class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    comment_owner = models.ForeignKey(User, blank=True)
    comment= models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)



class Likes(models.Model):
    liker=models.ForeignKey(User)
    image =models.ForeignKey(Image)