// Smart navbar: hide on scroll-down, reappear on scroll-up
// Only activates after scrolling past the initial hero area
var lastScroll = 0;

$(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll <= 0) {
        $('.navbar').removeClass('navbar-hide');
        lastScroll = scroll;
        return;
    }

    if (scroll > lastScroll) {
        // Scrolling down — hide navbar
        $('.navbar').addClass('navbar-hide');
    } else {
        // Scrolling up — show navbar
        $('.navbar').removeClass('navbar-hide');
    }

    lastScroll = scroll;
});

/* Close expanded mobile navbar when a non-dropdown nav-item is clicked */
$('.nav-item:not(#excluir1,#excluir2)').click(function () {
    if ($('#btnCollapse').css('display') !== 'none')
        $('#btnCollapse').click();
});
