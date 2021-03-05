from .models import Purchase
from django.forms import ModelForm, DateInput, TextInput, NumberInput, Textarea, DateTimeField, ChoiceField, Select
import datetime


class PurchaseForm(ModelForm):
    date = DateTimeField(input_formats=['%d.%m.%Y'], initial=format(datetime.date.today(), '%d.%m.%Y'), widget=DateInput(attrs={'placeholder': 'Дата покупки', 'class': 'form-control'}))
    pur_choices = (
        ("1", "Совместная покупка"),
        ("0", "Покупка в одиночку"),
    )
    join_purchase = ChoiceField(choices=pur_choices, widget=Select(attrs={'label': 'Совместная покупка', 'class': 'form-control'}))

    class Meta:
        model = Purchase
        fields = ["date", "product", "join_purchase", "amount", "price", "note"]
        widgets = {
            "product": TextInput(attrs={
                'placeholder': 'Продукт',
                'class': 'form-control',
                'autofocus': 'autofocus'
            }),
            "amount": NumberInput(attrs={
                'placeholder': 'Количество',
                'class': 'form-control',
                'value': '1'
            }),
            "price": NumberInput(attrs={
                'placeholder': 'Цена',
                'class': 'form-control'
            }),
            "note": Textarea(attrs={
                'placeholder': 'Заметка',
                'class': 'form-control'
            })
        }
