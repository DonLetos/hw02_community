from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Contact

# IEA:: get model 'User'
User = get_user_model()


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('first_name', 'last_name', 'username', 'email')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')

    # Метод-валидатор для поля subject
    def clean_subject(self):
        data = self.cleaned_data['subject']
        if 'спасибо' not in data.lower():
            text_message = 'Вы обязательно должны нас поблагодарить!'
            raise forms.ValidationError(text_message)
        return data
