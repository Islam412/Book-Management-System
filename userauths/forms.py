from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User , Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'First Name'}), max_length=100, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'Last Name'}), max_length=100, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'Username'}), max_length=100, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': '' , 'id': "", 'placeholder':'Email Address'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "", 'placeholder':'Password'}), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'with-border'
            



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cover_images', 'phone', 'address']
        widgets = {
            'cover_images': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        }
