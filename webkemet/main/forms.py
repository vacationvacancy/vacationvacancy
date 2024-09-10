from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    receive_emails = forms.BooleanField(required=False, label="Would you like to recieve emails on dev updates and game news?")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")