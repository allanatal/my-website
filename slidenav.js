$(".dropdown").on("hide.bs.collapse", function() {
    $(this).find(".dropdown-menu").first().addClass( "sliding" )
});
$(".dropdown").on("hidden.bs.collapse", function() {
    $(this).find(".dropdown-menu").first().removeClass( "sliding" )
});
$(document).click(function() {
    $(".dropdown-menu.collapse.show").collapse("hide");
});

/* https://coderatings.io/snippet/96/add-smooth-sliding-animation-to-bootstrap-4-dropdown-menu */