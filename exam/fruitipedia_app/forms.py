from django import forms
from .models import ProfileModel, FruitModel


class ProfileCreateModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        labels ={
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

class ProfileEditModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }



class FruitCreateModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'

        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition',
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        exclude = ['nutrition']

        widgets = {
            'name': forms.TextInput(attrs={'disabled': 'disabled'}),
            'image_url': forms.URLInput(attrs={'disabled': 'disabled'}),
            'description': forms.Textarea(attrs={'disabled': 'disabled'})

        }
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
        }

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

