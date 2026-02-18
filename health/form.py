from django import forms

class ScanForm(forms.Form):
    barcode = forms.CharField(max_length=50, label="Enter Product Barcode")
