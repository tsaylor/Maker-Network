import django.forms as forms
from general.models import UserProfile, Organization

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    def __init__(self, *args, **kw):
        super(UserProfileForm, self).__init__(*args, **kw)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

        self.fields.keyOrder = [
            'first_name', 'last_name', 'email',
            'city', 'state', 'postal_code', 'url'
            ]

    def save(self, *args, **kw):
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.user.save()
        return super(UserProfileForm, self).save(*args, **kw)

    class Meta:
        model = UserProfile
        exclude = ('user', 'image_height', 'image_width', 'skills', 'subscriptions')

class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ('members', 'admin', 'resources')
