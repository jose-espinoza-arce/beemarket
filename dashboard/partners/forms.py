from oscar.apps.dashboard.partners import forms

from partner.models import PartnerAddress

class PartnerAddressForm(forms.PartnerAddressForm):
    class Meta:
        fields = ['name', 'line1', 'line2', 'line3', 'line4',
                  'phone_number', 'state', 'postcode', 'country']
        model = PartnerAddress
