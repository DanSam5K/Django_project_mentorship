from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now()
        return context


class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
