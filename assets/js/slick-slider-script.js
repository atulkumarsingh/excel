//Playing with Ken Wheeler Slick carousel
$('.slick-slider').slick({
    //dots: true,
    infinite: true,
    arrows: true,
    centerMode: true,
    centerPadding: '12%',
    slidesToShow: 2,
    slidesToScroll: 1,
    speed: 500,
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


/* $(".slick-center").addClass(
		"switch");
$(".slick-current").prev().addClass(
		"switch");
$('.slick-slider').on('init', function(currentSlide) {
	console.log(currentSlide);
	$(".slick-center").prev().toggleClass("switch"); 
}); */
