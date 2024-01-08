from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from . import forms

User = get_user_model()

"""ログインページ"""
class CustomLoginView(LoginView):
    authentication_form = forms.CustomAuthenticationForm
    template_name = 'accounts/login.html'

"""ユーザー情報ページ"""
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


"""ユーザー情報変更ページ"""
class UserChangeView(UpdateView):
    model = User
    form_class = forms.UserChangeForm
    template_name = 'accounts/profile_change.html'

    def get_success_url(self):
        user_id = self.object.id
        return reverse('accounts:profile', kwargs={'pk': user_id})
    
    def get_object(self, queryset=None):
        return self.request.user

    def get_success_message(self, form):
        # save メソッドからインスタンスと変更されたフィールドのリストを取得
        changed_fields = form.change_fields()
        # 変更されたフィールドがあればメッセージを設定
        if changed_fields:
            changed_fields_str = ', '.join(changed_fields)
            messages.success(self.request, f"変更された項目: 「 {changed_fields_str} 」")
    
    def form_valid(self, form):
        form.save()
        self.get_success_message(form)
        return super().form_valid(form)