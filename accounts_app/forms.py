from django.contrib.auth.models import User
from django import forms

class EditProfileForm(forms.ModelForm):
   class Meta:
        model = User
        fields=[
        'first_name',
        'last_name',
        'email',
        ]

class VerificationForm(forms.Form):
    code = forms.CharField(label='Enter verfication code:',
                widget = forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'verfication code'
                    }
                )
            )

class LoginForm(forms.Form):
    username = forms.CharField(
                widget = forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder': 'username'
                    }
                )
            ) 
    password = forms.CharField(
                widget=forms.PasswordInput(
                    attrs={
                        'class':'form-control',
                        'placeholder': 'password'
                    }
                )
            )

class RegisterForm(forms.Form):
    first_name = forms.CharField(
                widget = forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder': 'first name'
                    }
                )
            )
    last_name = forms.CharField(
                widget = forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder': 'last name'
                    }
                )
            )
    username = forms.CharField(
                widget = forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder': 'username'
                        }
                    )
                )


    email    = forms.EmailField(
                widget=forms.EmailInput(
                    attrs={
                        'placeholder':'your email',
                        'class' :'form-control'
                        }
                    )
                )
    password = forms.CharField(
                widget=forms.PasswordInput(
                    attrs={
                        'class' :'form-control',
                        'placeholder':'password'
                        }
                    )
                )
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
                attrs={
                    'class' :'form-control',
                    'placeholder': 'confirm passsword'
                    }
                )
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('This this username has already taken')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('This email has already taken')
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password must match')
        return password