from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from apps.users.models import CustomUser

User = get_user_model()


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'display_name', 'avatar', 'password']


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'display_name',
            'avatar',
        )
