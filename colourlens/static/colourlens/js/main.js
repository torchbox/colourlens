$(function() {
  


  if ( !$('body').hasClass('ui-status-splash') ) {
    //Creates colour highligher on hover of a colour
    $('ul.colours li').hover(function() {
      //Reset any cloned items
      $('ul.colours li.cloned').remove();
      var left = $(this).offset().left;
      var cloned = $(this).clone();
      var width = $(this).width();
      $(cloned).addClass('cloned').css('position','absolute').css('left', left);
      $('ul.colours').append(cloned);
    });
  }


});