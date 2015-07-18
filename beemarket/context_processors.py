from oscar.core.loading import get_model

Wishlist = get_model('wishlists', 'WishList')
Line = get_model('wishlists', 'Line')


def wishlists(request):
    ctx = {}
    if getattr(request, 'user', None) and request.user.is_authenticated():
        wish_lists = Wishlist.objects.filter(
            owner=request.user)
        ctx['wish_lists'] = wish_lists
    return ctx

#def wishlines(request):
#    ctx = {}
#    if getattr(request, 'user', None) and request.user.is_authenticated():

