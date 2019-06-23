from django import forms
from django.contrib.auth.models import User

from StudentInfo.models import Course


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    from django.contrib.auth.models import User
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                            widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
         raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


from django import forms

class CourseForm(forms.Form):
    course_title = forms.CharField()
    duration = forms.CharField()
    credit_hours = forms.IntegerField()
    syllabus = forms.FileField()


class SectionForm(forms.Form):
    name = forms.CharField()
    course = forms.ModelChoiceField(queryset=Course.objects.all())