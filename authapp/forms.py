import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SignupForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    age = forms.IntegerField()
    detailed_address = forms.CharField(widget=forms.Textarea)
    id_proof_choices = [
        ('Aadhar Card', 'Aadhar Card'),
        ('Pancard', 'Pancard'),
        ('Other', 'Other'),
    ]
    id_proof = forms.ChoiceField(choices=id_proof_choices)
    id_proof_upload = forms.ImageField()
    country = forms.CharField(max_length=100, initial='India', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    pass1 = forms.CharField(widget=forms.PasswordInput, label='Your Password')
    pass2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')

        if pass1 != pass2:
            raise forms.ValidationError(_("Passwords do not match"))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError(_("Email is already taken"))
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise forms.ValidationError(_("Name should contain only letters and spaces"))
        return name

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not re.match(r'^[A-Za-z\s]+$', city):
            raise forms.ValidationError(_("City should contain only letters and spaces"))
        return city

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if not re.match(r'^[A-Za-z\s]+$', state):
            raise forms.ValidationError(_("State should contain only letters and spaces"))
        return state

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{10}$', phone_number):
            raise forms.ValidationError(_("Phone number should contain exactly 10 digits"))
        return phone_number

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not str(age).isdigit():
            raise forms.ValidationError(_("Age should be a number"))
        if int(age) > 100:
            raise forms.ValidationError(_("Age should not exceed 100"))
        return age

    def clean_id_proof_upload(self):
        id_proof_upload = self.cleaned_data.get('id_proof_upload')

        if id_proof_upload:
            # Check file size (limit to 10MB)
            if id_proof_upload.size > 10 * 1024 * 1024:
                raise forms.ValidationError(_("File size should be less than 10MB."))

            # Check file format (allow JPG, PNG, and PDF)
            allowed_formats = ['image/jpeg', 'image/png', 'application/pdf']
            if id_proof_upload.content_type not in allowed_formats:
                raise forms.ValidationError(_("Invalid file format. Only JPG, PNG, and PDF formats are allowed."))

        return id_proof_upload

    def clean_pass1(self):
        pass1 = self.cleaned_data.get('pass1')

        # Check if password contains at least one numeric character
        if not re.search(r'\d', pass1):
            raise forms.ValidationError(_("Password should contain at least one numeric character."))

        # Check if password contains at least one alphabetic character
        if not re.search(r'[a-zA-Z]', pass1):
            raise forms.ValidationError(_("Password should contain at least one alphabetic character."))

        # Check if password contains at least one special character (non-alphanumeric)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
            raise forms.ValidationError(_("Password should contain at least one special character."))

        # Check if the password meets the length criteria (8 to 14 characters)
        if len(pass1) < 8 or len(pass1) > 14:
            raise forms.ValidationError(_("Password should be between 8 and 14 characters long."))

        return pass1
