import random
import string

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



from config.settings import EMAIL_HOST_USER

from users.forms import UserRegistrForm, UserProfileForm
from users.models import User

# Create your views here.

class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):

    model = User
    form_class = UserRegistrForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject="поздравляю с регистрацией",
            message="вы зарегистировались",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]

        )
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):

            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('product_list')

        return redirect('users:invalid_verify')
@login_required
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])

            send_mail(
                subject='Ваш новый пароль',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )

            user.set_password(new_password)
            user.save()

            return redirect(reverse('users:login'))
        except User.DoesNotExist:
            message = 'Мы не можем найти пользователя с этим адресом электронной почты'
            context = {
                'message': message
            }
            return render(request, 'users/forgot_password.html', context)
    else:
        return render(request, 'users/forgot_password.html')