import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage, send_mail
from django.forms import ModelForm, EmailField, EmailInput
from smtplib import SMTP
from .models import CustomUser


# ロガーの設定
logger = logging.getLogger(__name__)


"""ログイン"""
class CustomAuthenticationForm(AuthenticationForm):
    username = EmailField(label="Eメールアドレス", widget=EmailInput(
        attrs={'class': 'form-control', 'placeholder': '', 'required': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


"""サインアップ"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['password1'].help_text = ''
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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


class ContactForm(forms.Form):
    name = forms.CharField(
        label="お名前",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "お名前",
            }
        )
    )

    email = forms.EmailField(
        label="メールアドレス",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレス",
            }
        )
    )

    subject = forms.CharField(
        label="件名",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "件名",
            }
        )
    )

    message = forms.CharField(
        label="お問合わせ内容",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "お問合わせ内容",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user and isinstance(user, CustomUser):
            self.fields['name'].initial = user.username
            self.fields['email'].initial = user.email

    def createMIMEText(self):
        user_email = self.cleaned_data['email']
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        to_email = settings.DEFAULT_FROM_EMAIL


        # MIMETextを作成
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = user_email
        msg['To'] = to_email

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        return msg
    
    def test_send_email(self):
        send_mail(
            'テストメールの件名',
            'これはテストメールの本文です。',
            'test@test.com',
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
            )
    
    def send_email(self):
        try:
            account = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD

            host = settings.EMAIL_HOST

            port = settings.EMAIL_PORT

            # サーバーを指定
            server = SMTP(host, port)
            server.starttls()

            # ログイン処理
            server.login(account, password)

            msg = self.createMIMEText()

            # メール送信
            server.send_message(msg)
        except Exception as e:
            # ここでエラーログを記録
            logger.error(f"メール送信エラー", exc_info=True)
        finally:
            # 閉じる
            if 'server' in locals():
                server.quit()