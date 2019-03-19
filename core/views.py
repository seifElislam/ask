from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.models import User


class Login(View):
    """
    Login view
    """
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     permission_classes = [Or(IsSystemAdmin, IsCollaborator, IsAdmin, IsAdminUser, AllowAny)]
    #     return [permission() for permission in permission_classes]

    @staticmethod
    def get(request):
        """
        Render login page
        """
        return render(request, 'core/login.html')

    @staticmethod
    def post(request):
        """
        Authenticate a user
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'core/home.html')
        else:
            return render(request, 'core/login.html')


class Home(View):
    """
    Login view
    """
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     permission_classes = [Or(IsSystemAdmin, IsCollaborator, IsAdmin, IsAdminUser, AllowAny)]
    #     return [permission() for permission in permission_classes]

    @staticmethod
    def get(request):
        """
        Render home page for authenticated users only
        """
        if request.user.is_anonymous:
            return render(request, 'core/login.html')
        return render(request, 'core/home.html')

    # @staticmethod
    # def post(request):
    #     """
    #     Submit e-mail form
    #     """
    #     # email = request.POST['email']
    #     try:
    #         # account = User.objects.get(email=email)
    #         # token = generate_confirmation_token(account.id)
    #         # send_email(email, token)
    #         return render(request, 'core/home.html')
    #     except User.DoesNotExist:
    #         return render(request, 'core/login.html')


class Register(View):
    """

    """

    @staticmethod
    def get(request):
        """
        Render home page for authenticated users only
        """
        return render(request, 'core/register.html')

    @staticmethod
    def post(request):
        """
        Register new users
        """
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmed_password = request.POST.get('confirmPassword')
        print(username, email, password, confirmed_password)
        if not email:
            return render(request, 'core/register.html', {'error_msg': 'Please fill all the form'})
        try:
            if User.objects.get(email=email) or User.objects.get(username=username):
                return render(request, 'core/register.html', {'error_msg': 'A user has register with this info'})
        except User.DoesNotExist:
            pass
        if password != confirmed_password:
            return render(request, 'core/register.html', {'error_msg': 'Passwords didn\'t match'})
        User.objects.create_user(username=username, email=email, password=password)
        return render(request, 'core/login.html')


