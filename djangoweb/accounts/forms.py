from django import forms as auth_forms
from django.forms import ImageField, FileInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

from djangoweb.accounts.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        #fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name')
        field_classes = {
            'username': UsernameField,
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email')
        exclude = ('password',)
        labels = {'username': 'Username: ',
                  'first_name': 'First Name: ',
                  'last_name': 'Last Name: ',
                  'email': 'Email: ',
                  }
        field_classes = {
            'username': UsernameField,
        }


class ProfileEditForm(auth_forms.ModelForm):
    profile_picture = ImageField(widget=FileInput)

    class Meta:
        model = Profile
        fields = ('profile_picture', 'description')
