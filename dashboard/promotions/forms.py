from oscar.apps.dashboard.promotions.forms import PagePromotionForm as CorePagePromotionForm, PagePromotion


class PagePromotionForm(CorePagePromotionForm):
    class Meta:
        model = PagePromotion
        fields = ['position', 'page_url']
