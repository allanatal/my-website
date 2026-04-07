document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = this.getAttribute('href');
        if (target === '#') return;
        const el = document.querySelector(target);
        if (!el) return;
        e.preventDefault();
        el.scrollIntoView({ behavior: 'smooth' });
    });
});

/* Acima:  https://stackoverflow.com/questions/7717527/smooth-scrolling-when-clicking-an-anchor-link?answertab=active#tab-top */

/* Abaixo: botão back to top: https://codepen.io/michalwyrwa/pen/GBaPPj */

$(document).ready(function(){
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        }
        else {
            $('#back-to-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#back-to-top').click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 400);
    return false;
    });
});
