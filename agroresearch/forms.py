from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from .models import LeakReport

# Registration Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    full_name = forms.CharField(max_length=30)  # Changed to mandatory field
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Account
        fields = ("email", "username", "full_name", "phone_number", "password1", "password2")


# Account Authentication Form
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password. Please try again.")
            if not user.is_active:
                raise forms.ValidationError("This account is inactive. Please contact support.")

        return cleaned_data


# Account Update Form
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("email", "full_name",)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email field cannot be empty.")
        if Account.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(f'Email "{email}" is already in use.')
        return email.lower()  # Ensures email is in lowercase


# Leak Report Form
class LeakReportForm(forms.ModelForm):
    class Meta:
        model = LeakReport
        fields = ['leak_type', 'description', 'latitude', 'longitude']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Eleza kwa kifupi hitilafu...'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("Please provide a description of the leak.")
        return description
