from django.conf.urls import url

from dashboard.catalogue import views

from oscar.core.application import Application
from oscar.core.loading import get_class

from oscar.apps.dashboard.catalogue import app

class CatalogueApplication(app.CatalogueApplication):

    def get_urls(self):

        urls = super(CatalogueApplication, self).get_urls()

        urls += [
            url(r'^brand/create/$',
                views.BrandCreateView.as_view(),
                name='catalogue-brand-create'),
            url(r'^brand/$',
                views.BrandListView.as_view(),
                name='catalogue-brand-list'),
            url(r'^brand/(?P<pk>\d+)/update/$',
                views.BrandUpdateView.as_view(),
                name='catalogue-brand-update'),
            url(r'^brand/(?P<pk>\d+)/delete/$',
                views.BrandDeleteView.as_view(),
                name='catalogue-brand-delete'),
        ]


        return self.post_process_urls(urls)


application = CatalogueApplication()
