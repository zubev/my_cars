from django import forms

from accounts.choices import REGIONS
from cars.models import Car, Report
from cars.choices import BRANDS


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('user',)
        widgets = {
            'model': forms.Select(),
        }


class FilterForm(forms.Form):
    CHOICES = (
        ('', ''),
        (1, 1),
        (2, 2),
        (18, 18),

    )

    brand = forms.ChoiceField(choices=BRANDS, required=False)
    models = forms.ChoiceField()
    year = forms.IntegerField(required=False, min_value=1960, max_value=2022)
    max_price = forms.IntegerField(min_value=1, required=False)
    region = forms.ChoiceField(required=False, choices=REGIONS)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ('car','added_by',)
        widgets = {
            'massage': forms.Textarea()
        }
