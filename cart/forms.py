from django import forms


# this creates a HTML form.
class QtyForm(forms.Form):
    qty = forms.IntegerField(label='Quantity', min_value=0, default=1)
