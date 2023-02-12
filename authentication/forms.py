from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'The user with username {username} does not exist!')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Password is not correct!')


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'User name or login'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }
