from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from djangoweb.accounts.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'testuser',
        'password': '12345qew',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
    }

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
