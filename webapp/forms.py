from django import forms
from .models import stepOneModel

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class myForm(forms.ModelForm):

    class Meta:
        model = stepOneModel
        fields = '__all__'

        widgets = {
        'fullName':forms.TextInput(attrs={'class':'form-control m-input'}),
        'emailAddress':forms.TextInput(attrs={'class':'form-control m-input'}),
        'contact':forms.TextInput(attrs={'class':'form-control m-input'}),
        'amount':forms.TextInput(attrs={'class':'form-control m-input'}),

        }
    