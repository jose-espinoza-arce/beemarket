from catalogue.models import Brand
from dashboard.catalogue.forms import BrandForm

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from django.views import generic


class BrandCreateUpdateView(generic.UpdateView):

    template_name = 'dashboard/catalogue/brand_form.html'
    model = Brand
    form_class = BrandForm
    #product_attributes_formset = ProductAttributesFormSet

    def process_all_forms(self, form):
        """
        This validates both the ProductClass form and the
        ProductClassAttributes formset at once
        making it possible to display all their errors at once.
        """
        if self.creating and form.is_valid():
            # the object will be needed by the product_attributes_formset
            self.object = form.save(commit=False)

        #attributes_formset = self.product_attributes_formset(
        #    self.request.POST, self.request.FILES, instance=self.object)

        is_valid = form.is_valid() #and attributes_formset.is_valid()

        if is_valid:
            return self.forms_valid(form)  #, attributes_formset)
        else:
            return self.forms_invalid(form)  #, attributes_formset)

    def forms_valid(self, form):#, attributes_formset):
        form.save()
        #attributes_formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, form):#, attributes_formset):
        messages.error(self.request,
                       _("Your submitted data was not valid - please "
                         "correct the errors below"
                         ))
        ctx = self.get_context_data(form=form)#,
                                    #attributes_formset=attributes_formset)
        return self.render_to_response(ctx)

    form_valid = form_invalid = process_all_forms

    def get_context_data(self, *args, **kwargs):
        ctx = super(BrandCreateUpdateView, self).get_context_data(
            *args, **kwargs)

        #if "attributes_formset" not in ctx:
        #    ctx["attributes_formset"] = self.product_attributes_formset(
        #        instance=self.object)

        ctx["title"] = self.get_title()

        return ctx


class BrandCreateView(BrandCreateUpdateView):

    creating = True

    def get_object(self):
        return None

    def get_title(self):
        return _("Add a new brand")

    def get_success_url(self):
        messages.info(self.request, _("Brand created successfully"))
        return reverse("dashboard:catalogue-brand-list")


class BrandUpdateView(BrandCreateUpdateView):

    creating = False

    def get_title(self):
        return _("Update Brand '%s'") % self.object.name

    def get_success_url(self):
        messages.info(self.request, _("Brand updated successfully"))
        return reverse("dashboard:catalogue-brand-list")

    def get_object(self):
        product_class = get_object_or_404(Brand, pk=self.kwargs['pk'])
        return product_class


class BrandListView(generic.ListView):
    template_name = 'dashboard/catalogue/brand_list.html'
    context_object_name = 'classes'
    model = Brand

    def get_context_data(self, *args, **kwargs):
        ctx = super(BrandListView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Product Types")
        return ctx


class BrandDeleteView(generic.DeleteView):
    template_name = 'dashboard/catalogue/brand_delete.html'
    model = Brand
    form_class = BrandForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(BrandDeleteView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Delete Brand '%s'") % self.object.name
        product_count = self.object.products.count()

        if product_count > 0:
            ctx['disallow'] = True
            ctx['title'] = _("Unable to delete '%s'") % self.object.name
            messages.error(self.request,
                           _("%i products are still assigned to this brand") %
                           product_count)
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Brand deleted successfully"))
        return reverse("dashboard:catalogue-brand-list")