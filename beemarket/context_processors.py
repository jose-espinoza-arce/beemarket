from oscar.core.loading import get_model

Wishlist = get_model('wishlists', 'WishList')
Line = get_model('wishlists', 'Line')


def wishlists(request):
    ctx = {}
    if getattr(request, 'user', None) and request.user.is_authenticated():
        wish_lists = Wishlist.objects.filter(
            owner=request.user)
        if wish_lists:
            ctx['wish_list'] = wish_lists[0]

    return ctx

#def wishlines(request):
#    ctx = {}
#    if getattr(request, 'user', None) and request.user.is_authenticated():

