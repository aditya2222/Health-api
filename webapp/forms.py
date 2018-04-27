from django import forms
from .models import formModel

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class myForm(forms.ModelForm):

    class Meta:
        model = formModel
        fields = '__all__'

        widgets = {
        'ProvisionalDiagnosis':forms.SelectMultiple(),
        'FamilyHistory':forms.SelectMultiple(),
        'Name':forms.TextInput(attrs={'class':'form-control m-input','id':'name'}),
        'Kureid':forms.TextInput(attrs={'class':'form-control m-input','readonly':'true',}),
        'ChiefComplaints':forms.TextInput(attrs={'class':'form-control m-input',}),
        'Examinedby':forms.TextInput(attrs={'class':'form-control m-input',}),
        'Verifiedby':forms.TextInput(attrs={'class':'form-control m-input',}),
        'PastHistory':forms.TextInput(attrs={'class':'form-control m-input','name':'PastHistory'}),
        'ChiefComplaints':forms.SelectMultiple(),
        'PastHistory':forms.SelectMultiple(),
        
       

        }


    