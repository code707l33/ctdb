from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from .views import signup, signup_with_account_and_password, signup_with_email, profile_change
from .forms import EmailValidationOnForgotPasswordForm, LoginForm


app_name = 'accounts'

# Built-in views from django.contrib.auth.urls with a little customization applied.
urlpatterns = [
    path('login/', LoginView.as_view(form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(
        success_url=reverse_lazy('accounts:password_change_done')), name='password_change'
    ),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPasswordForm, success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Custom views about signup.
urlpatterns += [
    path('signup/', signup, name='signup'),
    path(
        'signup/with-chief-email/',
        signup_with_email,
        kwargs={'email_endswith_strings': ['@chief.com.tw']},
        name='signup_with_chief_email'
    ),
]

# Custom views about user extending model - profile.
urlpatterns += [
    path('profile/', profile_change, name='profile_change'),
]
