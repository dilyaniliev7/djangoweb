from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from djangoweb.accounts.models import Profile
from djangoweb.djangogram.models import PhotoLike, PhotoComment
from djangoweb.photos.models import Photo

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'TestUser',
        'email': 'testuser@abv.bg',
        'password': '12345qew',
    }
    VALID_LOGIN_CREDENTIALS = {
        'email': 'testuser@abv.bg',
        'password': '12345qew',
    }
    VALID_USER_CREDENTIALS_2 = {
        'username': 'Testuser2',
        'email': 'user2@abv.bg',
        'password': 'password123'
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
    }

    def assertEmpty(self, collection):
        return self.assertEqual(0, len(collection), 'It is not empty')

    def create_photo_for_user(self, user):
        result = Photo.objects.create(
            user=user,
            photo='test_photo',
            description='Test description',
            location='Test location'
        )
        return result

    def __create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)

        self.client.login(**self.VALID_LOGIN_CREDENTIALS)

        return user

    def test_when_opening_not_existing_user_profile__expect_404(self):
        user = UserModel.objects.create_user(email='testuser@abv.bg', password='12345')
        self.client.force_login(user)
        response = self.client.get(reverse('details user', kwargs={
            'pk': 60,
        }))

        self.assertEqual(404, response.status_code)

    def test_when_all_valid__expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        response = self.client.get(reverse('details user', kwargs={
            'pk': profile.pk,
        }))
        self.assertTemplateUsed('profile/profile-details-page.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])


    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        profile_user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS_2)

        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_when_user_has_no_photos_to_be_correct(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['user_photos'])

    def test_when_user_has_at_least_one_photo_expect_to_be_true(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        self.create_photo_for_user(user)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertIn('user_photos', response.context)
        self.assertGreater(len(response.context['user_photos']), 0)

        self.assertEqual(response.context['user_photos'][0].description, 'Test description')
        self.assertEqual(response.context['user_photos'][0].location, 'Test location')

    def test_when_photo_has_at_least_one_like(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        photo = self.create_photo_for_user(user)
        PhotoLike.objects.create(to_photo=photo, user=user)
        likes_count = PhotoLike.objects.filter(to_photo=photo).count()
        self.assertGreater(likes_count, 0)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

    def test_when_photo_has_zero_likes(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        photo = self.create_photo_for_user(user)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(response.context['likes_count'][0], 0)

    def test_when_photo_has_zero_comments(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        photo = self.create_photo_for_user(user)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(response.context['comments_count'], 0)

    def test_when_photo_has_at_least_one_comment_expect_to_be_true(self):
        user = self.__create_user_and_login(self.VALID_USER_CREDENTIALS)

        photo = self.create_photo_for_user(user)

        PhotoComment.objects.create(photo=photo, user=user)
        comments_count = PhotoComment.objects.filter(photo=photo).count()
        self.assertGreater(comments_count, 0)