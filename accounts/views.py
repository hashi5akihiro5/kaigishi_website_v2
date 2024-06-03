from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView

from . import forms

# from django.views.decorators.csrf import requires_csrf_token
# from django.http import HttpResponseServerError

User = get_user_model()


# 本番環境でエラーを表示する
# @requires_csrf_token
# def my_customized_server_error(request, template_name='500.html'):
#     import sys
#     from django.views import debug
#     error_html = debug.technical_500_response(request, *sys.exc_info()).content
#     return HttpResponseServerError(error_html)


"""ログインページ"""


class CustomLoginView(LoginView):
    authentication_form = forms.CustomAuthenticationForm
    template_name = "accounts/login.html"


"""サインアップページ"""


class SignupView(FormView):
    form_class = forms.CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # ユーザーを保存
        user = form.save(commit=False)
        user.save()

        # 認証
        user = authenticate(
            username=user.email,
            password=form.cleaned_data["password1"],
        )
        return super().form_valid(form)


"""ユーザー情報ページ"""


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


"""ユーザー情報変更ページ"""


class UserChangeView(UpdateView):
    model = User
    form_class = forms.UserChangeForm
    template_name = "accounts/profile_change.html"

    def get_success_url(self):
        user_id = self.object.id
        return reverse("accounts:profile", kwargs={"pk": user_id})

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_message(self, form):
        # save メソッドからインスタンスと変更されたフィールドのリストを取得
        changed_fields = form.change_fields()
        # 変更されたフィールドがあればメッセージを設定
        if changed_fields:
            changed_fields_str = ", ".join(changed_fields)
            messages.success(
                self.request, f"変更された項目: 「 {changed_fields_str} 」"
            )

    def form_valid(self, form):
        form.save()
        self.get_success_message(form)
        return super().form_valid(form)


"""お問合せ画面"""


class ContactFormView(FormView):
    template_name = "accounts/contact.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy("accounts:contact_result")

    def get_form_kwargs(self):
        kwargs = super(ContactFormView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = "accounts/contact_result.html"
