from django.forms import ModelForm
from general.models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'image_height', 'image_width')
