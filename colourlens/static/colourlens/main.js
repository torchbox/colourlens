$(document).ready(function() {
    var total_palette = window.totalPalette;

    $('#colour-list div a').each(function(i, ele) {
        var h = $(ele).text();
        var log = Math.log(h) * 20;
        $(ele).parent().css('height', (log + 11) + 'px');
        $(ele).css('visibility', 'visible');
        ele.innerHTML = '';    
    });
    // /$('.section').css('height', $( window ).height())
    $('#colour-page div a').each(function(i, ele) {
        var h = $(ele).height();
        var sqrt = Math.log(h) * 10;
        $(ele).parent().css('height', $(window).height());
        ele.innerHTML = '';    
    });
    $('.explorerGrid h3, .explorerGrid p.artist, .explorerGrid span.institution').hide();
    $('#fullpage').fullpage();
});
