import form as form
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

from accounts.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number', False)
    #     try:
    #         int(phone_number)
    #         return phone_number
    #     except:
    #         raise forms.ValidationError('Enter a valid number')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()

    )
