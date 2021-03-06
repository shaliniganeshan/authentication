from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import RadioSelect


class RegistrationForm(UserCreationForm):
	class Meta:
              model = User
		fields = {'username',
                          'first_name',
                          'last_name',
                          'email',}
		 

                def save(self,commit= True):
                    user = super(RegistrationForm,self).save(commit=False)
                    user.user_name = self.cleaned_data['username']
                    user.first_name = self.cleaned_data['first_name']
                    user.last_name = self.cleaned_data['last_name']
                    user.email = self.cleaned_data['email'] 
                    
                    if commit:
                        user.save()
                    return user
                
