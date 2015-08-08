from oscar.apps.address.abstract_models import AbstractPartnerAddress

from phonenumber_field.modelfields import PhoneNumberField as CorePhoneNomberField

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from phonenumber_field.validators import validate_international_phonenumber
from phonenumber_field.phonenumber import to_python
from django.forms.fields import CharField


class PhoneNumberFormField(CharField):
    default_error_messages = {
        'invalid': _('Enter a valid phone number including country code (ex. +529999999999).'),
    }
    default_validators = [validate_international_phonenumber]

    def to_python(self, value):
        phone_number = to_python(value)
        if phone_number and not phone_number.is_valid():
            raise ValidationError(self.error_messages['invalid'])
        return phone_number

    def widget_attrs(self, widget):
        attrs = super(CharField, self).widget_attrs(widget)
        attrs.update({'placeholder': '+529999999999'})

        return attrs


class PhoneNumberField(CorePhoneNomberField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': PhoneNumberFormField,
        }
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)



class PartnerAddress(AbstractPartnerAddress):
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'))

from oscar.apps.partner.models import *
