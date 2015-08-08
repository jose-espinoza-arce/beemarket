# -*- coding: utf-8 -*-
from haystack import indexes

from django.utils.translation import ugettext_lazy as _

from oscar.apps.search.search_indexes import ProductIndex as CoreProductIndex


class ProductIndex(CoreProductIndex):
    brand = indexes.CharField(null=True, faceted=True)
    attribute = indexes.MultiValueField(null=True, faceted=True)
    attributevalue = indexes.MultiValueField(null=True, faceted=True)

    def prepare_brand(self, obj):
        if obj.brand:
            return obj.brand.name
        else:
            return _('No brand')

    def prepare_attribute(self, obj):
        #print 'en el prepare de attr'
        attributes = obj.attributes.all()
        #print attributes
        if len(attributes) > 0:
            #print attributes
            return [attribute.name for attribute in attributes]
        else:
            return []

    def prepare_attributevalue(self, obj):
        attrvalues = obj.attribute_values.all()
        if len(attrvalues) > 0:
            list = []
            for attrvalue in attrvalues:
                value = attrvalue.value_as_text #getattr(attrvalue, 'value_%s' % attrvalue.attribute.type)
                attr = attrvalue.attribute.name
                list += ['%s:%s' % (attr, value)]
                print list
                #print value.type
            return list
        else:
            return []