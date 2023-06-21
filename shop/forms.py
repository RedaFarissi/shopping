from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#UserCreationForm is class provided by django to handle Creation User by default give you user name and password1 and password2
class SignUpForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    class Meta:
        model = User
        # we add email to Creation User 
        fields = ('username', 'email', 'password1', 'password2')