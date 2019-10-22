from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User
class TestProfile(TestCase):
   def setUp(self):
       self.user = User(username='David')
       self.user.save()
       self.profile_test = Profile( profile_pic=' media/sweet-food-chocolate-wallpaper-e45943b31955e9eb66381700fb22297d_hTxbvq4.jpg', bio='this is a test ', user=self.user)
   def test_instance(self):
       self.assertTrue(isinstance(self.profile_test, Profile))
   def test_profile_save(self):
       self.profile_test.profile_save()
       travel = Profile.objects.all()
   def tearDown(self):
       '''
       Test delete category behaivour
       '''
       Profile.objects.all().delete()
   def test_delete_profile(self):
       '''
       Test if category can be deleted from db.
       '''
       self.profile_test.profile_save()
       self.profile = Profile.objects.get(id = 1)
       self.assertFalse(len(Profile.objects.all()) == 0)




class ImageTestClass(TestCase):
    """test class for Image model"""

    def setUp(self):

        self.user = User.objects.create_user("testuser")

        self.new_profile = Profile(profile_pic='media/sweet-food-chocolate-wallpaper-e45943b31955e9eb66381700fb22297d_hTxbvq4.jpg',bio="this is a test bio",
                                     user=self.user)
        self.new_profile.save()

        self.new_image = Image(pic='media/315444-photography-children-happy-748x499_IV3bpoa.jpg',
                               caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

class CommentTestClass(TestCase):

    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_pic='media/sweet-food-chocolate-wallpaper-e45943b31955e9eb66381700fb22297d_hTxbvq4.jpg',
                                     bio="this is a test bio",
                                     user=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='media/315444-photography-children-happy-748x499_IV3bpoa.jpg',
                               caption="this is a test image", profile='')
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="this is a comment on a post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()









