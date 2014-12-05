$(function() {

    //Init jQuery UI tabs
    $('.colour-selector').tabs();
  
    //Set the colour strip heights
    function setColourPickerHeight() {
        var winHeight = $(window).height();
        var headerHeight = $('header.site-header').height();
        $('.ui-tabs-panel li').each(function( index ) {
            //Make a random number
            var randNum = Math.floor(Math.random()*(3500-1000+1)+1000);
            $(this).animate({height: winHeight - headerHeight}, randNum);
        });
    }

    setColourPickerHeight();
   
    // Creates colour highligher on hover of a colour
    $('ul.colours li').hover(function() {
        if ( $('body').hasClass('ui-status-picker') ) {
            var left = $(this).offset().left;
            var cloned = $(this).clone();
            var width = $(this).width();
            //Set the selected status
            //But remove any old ones first
            $('ul.colours li').removeClass('selected');
            $(this).addClass('selected');
            //Reset any cloned items
            $('ul.colours li.cloned').remove();
            $(cloned).addClass('cloned').css('position','absolute').css('left', left);
            $('ul.colours').append(cloned);
        }
    });

    //Fade out the mag glass
    $('.ui-status-splash .mag-glass h2').delay(2000).fadeOut(1000);
    $('.ui-status-splash .mag-glass').delay(2500).fadeOut(1400, function() {
        $('body').removeClass('ui-status-splash').addClass('ui-status-picker');
    });

    //Progress artwork picker state
    $(document).on('click','.colours li.cloned a',function() {
        $('body').removeClass('ui-status-picker').addClass('ui-status-artwork-pick');
        $('#colour-search li.cloned').fadeOut(100).remove();
        $('#colour-search li').each(function( index ) {
            $(this).animate({height: '80px' }, 1200);
        });
        var hex = $(this).data('hex-value');
        $('.colours').find('li.selected:not(.cloned) a[data-hex-value="'+hex+'"]').click();
    });


});