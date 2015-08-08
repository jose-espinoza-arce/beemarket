from django import forms

from catalogue.models import Brand, Product

from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['name', 'image']


class ProductForm(CoreProductForm):
    """
    Overrides ProductForm to add brand capability
    """
    class Meta:
        model = Product
        fields = [
            'title', 'upc', 'description', 'brand', 'is_discountable', 'structure']
        widgets = {
            'structure': forms.HiddenInput()
        }

