jQuery(document).ready(function ($) {
    $( "input" ).focus(function() {
        $('.has-error').hide();
    });
});
//$('input').on('keypress', function () { //1
