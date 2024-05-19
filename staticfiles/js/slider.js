$(document).ready(function() {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });

    $('.slider-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        centerMode: true,
        focusOnSelect: true
    });

    $('.slider-for').magnificPopup({
        delegate: 'img',
        type: 'image',
        gallery: {
            enabled: true
        },
        callbacks: {
            elementParse: function(item) {
                item.src = $(item.el).attr('src');
                item.w = $(item.el).data('width');
                item.h = $(item.el).data('height');
            }
        },
        fullscreen: {
            enabled: true
        }
    });
});
