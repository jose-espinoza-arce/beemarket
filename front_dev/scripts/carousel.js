/**
*
* Module carousel of minibasket
* Author: Jose
* Handles Carousel of minibasket.
*
**/


//---------Handler of the open/close carousel---------
$('div.dropdown.Minibasket a').on('click', function (event) {
    $(this).parent().toggleClass('open');
    if ($(this).parent().hasClass('open')) {
        setTimeout(function () {
            $('#basket-carousel').everslider({
                mode: 'carousel',
                moveSlides: 1
                //slideEasing: 'easeInOutCubic',
                //slideDuration: 700,
                //itemWidth: '200px'
            });
        }, 100);
    } else {
        var obj = $('#basket-carousel');
        console.log(obj);
    }


});

$('body').on('click', function (e) {
    if (!$('div.dropdown.Minibasket').is(e.target)
        && $('div.dropdown.Minibasket').has(e.target).length === 0
        && $('.open').has(e.target).length === 0
    ) {
        $('div.dropdown.Minibasket').removeClass('open');
    }
});


//--------------------------------------------------


