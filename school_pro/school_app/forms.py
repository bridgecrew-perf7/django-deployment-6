from django import forms
from school_app.models import UserProfile,User,Student

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('school_website','profile_pic')   

class StudentCreateView(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('__all__')