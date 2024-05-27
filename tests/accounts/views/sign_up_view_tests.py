# from django.test import TestCase
# from django.urls import reverse
#
#
# class SignUpViewTest(TestCase):
#     VALID_USER_DATA = {
#         'username': 'test_user',
#         'email': 'test_user@abv.bg',
#         'password1': 'password',
#         'password2': 'password',
#     }
#
#     def test_sign_up__when_valid_data__expect_logged_in_user(self):
#         response = self.client.post(
#             reverse('register'),
#             data=self.VALID_USER_DATA,
#             follow=True,
#         )
#         print(response.context)
#         self.assertEqual(self.VALID_USER_DATA['username'], response.context['email'].username)
