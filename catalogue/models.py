from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Brand(models.Model):
    """
    A model to represent the brand of a product.
    """

    name = models.CharField(_('Name'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='brands', blank=True,
                              null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Product(AbstractProduct):

    brand = models.ForeignKey('catalogue.Brand',
                              verbose_name=_('Brand'), null=True, blank=True,
                              related_name="products")

from oscar.apps.catalogue.models import *
