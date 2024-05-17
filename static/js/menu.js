$(document).ready(function() {
    $('.navbar-toggler').click(function() {
        $('.navbar-collapse').toggleClass('show');
    });

    $('.navbar-nav .nav-link').click(function() {
        $('.navbar-collapse').removeClass('show');
    });
});
