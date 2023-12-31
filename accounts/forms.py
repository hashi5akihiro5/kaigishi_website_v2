from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, EmailField, EmailInput
from .models import CustomUser


"""ログイン"""
class CustomAuthenticationForm(AuthenticationForm):
    username = EmailField(label="Eメールアドレス", widget=EmailInput(
        attrs={'class': 'form-control', 'placeholder': '', 'required': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


"""ユーザー情報編集"""
class UserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'last_name',
            'first_name',
            'email',
        )
        labels = {
            'username': 'ユーザー名',
            'last_name': '名 字',
            'first_name': '名 前',
            'email': 'メールアドレス',
        }

    def __init__(self, *args, **kwargs):
        # ユーザーの更新前情報をフォームに挿入
        super(UserChangeForm, self).__init__(*args, **kwargs)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError('この Eメールアドレス を持った Custom user が既に存在します。')
        return email
    
    def change_fields(self):
        # 変更されたフィールドを追跡するリスト
        changed_fields = []
        if self.initial.get('username') != self.cleaned_data.get('username'):
            changed_fields.append('ユーザー名')
        if self.initial.get('last_name') != self.cleaned_data.get('last_name'):
            changed_fields.append('名 字')
        if self.initial.get('first_name') != self.cleaned_data.get('first_name'):
            changed_fields.append('名 前')
        if self.initial.get('email') != self.cleaned_data.get('email'):
            changed_fields.append('メールアドレス')
        return changed_fields

    def save(self, commit=True):
        self.instance.username = self.cleaned_data['username']
        self.instance.first_name = self.cleaned_data['first_name']
        self.instance.last_name = self.cleaned_data['last_name']
        self.instance.email = self.cleaned_data['email']
        if commit:
            self.instance.save()
        return self.instance