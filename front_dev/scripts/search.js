/**
*
* Module carousel of minibasket
* Author: Jose
* Handles Carousel of minibasket.
*
**/
var SearchForm = (function ($){
    var search = {
        init: function(){
            this.cache();
            this.bind();
        },
        cache: function(){
            this.el = $('.Search--full')
            this.toggler = $('.Search-toggler');
        },
        bind: function(){
            var self = search;
            this.toggler.on('click', function (e) {
                e.preventDefault();
                self.el.toggleClass('isOpen');
                console.log($('.Search').has(e.target));
            });

            $('body').on('click', function (e) {
                if (!$('.Search').is(e.target)
                    && $('.Search').has(e.target).length === 0
                    && $('.isOpen').has(e.target).length === 0
                    ) {
                    $('.Search--full').removeClass('isOpen');
                }
            });
        }
    };
    return search;
})(jQuery);