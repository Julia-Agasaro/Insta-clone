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
    def search_username(cls,search_term):
        user = cls.objects.filter(user__username__icontains = search_term)

        return  user



class Image(models.Model):
    pic= models.ImageField(upload_to = 'media/')
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    

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

    


class Follow(models.Model):
    followings = models.ForeignKey(User,related_name='followee')
    followers = models.ForeignKey(User, related_name='follower')
  
    def __str__(self):
        return '{} follows {}'.format(self. followers , self.followings)


# Add following field to User dynamically
User.add_to_class('followings',
                  models.ManyToManyField('self',
                                         through=Follow,
                                         related_name='followers',
                                         symmetrical=False))