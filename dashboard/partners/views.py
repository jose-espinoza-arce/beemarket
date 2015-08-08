from oscar.apps.dashboard.partners import views
from oscar.apps.partner.models import Partner

from django.shortcuts import get_object_or_404

class PartnerUserUpdateView(views.PartnerUserUpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(PartnerUserUpdateView, self).get_context_data(**kwargs)
        ctx['partner'] = get_object_or_404(Partner,
                                           pk=self.kwargs['partner_pk'])
        return ctx