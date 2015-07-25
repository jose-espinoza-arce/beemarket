/**
*
* Module carousel of minibasket
* Author: Jose
* Handles Carousel of minibasket.
*
**/
var MiniBasket = (function ($) {
  var basket = {
    init: function(){
      this.cache();
      this.bind();
    },
    cache: function(){
      this.carousel = $('.MiniBasketCarousel');
      this.el = $('.MiniBasket--full');
      if (this.carousel.length>0) { this.carousel.slick( {
          slidesToShow: 4,
          slidesToScroll: 1,
          dots: true,
          centerMode: true,
          focusOnSelect: true,
          responsive: [
             {
               breakpoint: 768,
               settings: {
                 arrows: false,
                 centerMode: true,
                 centerPadding: '40px',
                 slidesToShow: 3
               }
             },
             {
               breakpoint: 480,
               settings: {
                 arrows: false,
                 centerMode: true,
                 centerPadding: '40px',
                 slidesToShow: 1
               }
             }
           ]
        }); 
      }
      this.toggler = $('.MiniBasket-toggler');
    },
    bind: function(){
      var self = basket;
      this.toggler.on('click', function (e) {
        e.preventDefault();
        self.el.toggleClass('isOpen');
      });
    }
  };
  return basket;
})(jQuery);





