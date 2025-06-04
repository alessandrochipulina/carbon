from django import forms

TRANSPORTE_CHOICES = [
    ('car', 'Car'),
    ('bike', 'Bike'),
    ('bus', 'Bus'),
    ('train', 'Train'),
]

COMBUSTIBLE_CHOICES = [
    ('diesel', 'Diesel'),
    ('petrol', 'Petrol'),
]

class HuellaCarbonoForm(forms.Form):
    transporte = forms.ChoiceField(choices=TRANSPORTE_CHOICES)
    pasajeros = forms.IntegerField(min_value=1)
    distancia = forms.FloatField(min_value=0)
    energia_kwh = forms.FloatField(min_value=0)
    gas_m3 = forms.FloatField(min_value=0)
    tipo_combustible = forms.ChoiceField(choices=COMBUSTIBLE_CHOICES)
    cantidad_combustible = forms.FloatField(min_value=0)