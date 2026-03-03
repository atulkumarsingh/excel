(function ($) {
    "use strict";

    if (typeof $.fn.slick !== "function") return;
    var $slider = $('.slick-slider');
    if (!$slider.length || $slider.hasClass('slick-initialized')) return;

    $slider.slick({
        infinite: true,
        arrows: true,
        centerMode: true,
        centerPadding: '12%',
        slidesToShow: 2,
        slidesToScroll: 1,
        speed: 560,
        autoplay: true,
        autoplaySpeed: 4000,
        pauseOnHover: true,
        pauseOnFocus: true,
        lazyLoad: 'ondemand',
        swipeToSlide: true,
        touchThreshold: 10,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                    centerPadding: '10%'
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                    centerPadding: '16%'
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    centerPadding: '8%'
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1,
                    centerPadding: '0'
                }
            }
        ]
    });
})(jQuery);


/* $(".slick-center").addClass(
		"switch");
$(".slick-current").prev().addClass(
		"switch");
$('.slick-slider').on('init', function(currentSlide) {
	console.log(currentSlide);
	$(".slick-center").prev().toggleClass("switch"); 
}); */
