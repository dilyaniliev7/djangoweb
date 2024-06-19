from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class SignUpViewTest(TestCase):

    def test_signup_view_renders(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        VALID_USER_DATA = {
            'username': 'test_user',
            'email': 'test_user@abv.bg',
            'password1': 'password',
            'password2': 'password',
        }
        response = self.client.post(reverse('register'), data=VALID_USER_DATA)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
