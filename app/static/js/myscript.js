Firebase.enableLogging(true);
var root = new Firebase('https://sud.firebaseio.com/');
var heading = root.child('Headings');
var data= {};
$(document).ready(function(){
	setupFirebase();
	// increment();

});
$('.carousel').carousel({
  interval: false
});


$(function() {

  "use strict";

  var topoffset = 50; //variable for menu height

  //Activate Scrollspy
  $('body').scrollspy({
    target: 'header .navbar',
    offset: topoffset
  });

  // // add inbody class
  // var hash = $(this).find('li.active a').attr('href');
  // if(hash !== '#featured') {
  //   $('header nav').addClass('inbody');
  // } else {
  //   $('header nav').removeClass('inbody');
  // }


  // // Add an inbody class to nav when scrollspy event fires
  $('.navbar-fixed-top').on('activate.bs.scrollspy', function() {
    var hash = $(this).find('li.active a').attr('href');
    if(hash !== '#featured') {
      $('header nav').addClass('inbody');
    } else {
      $('header nav').removeClass('inbody');
    }
  });


  //Use smooth scrolling when clicking on navigation
  $('.navbar a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') === 
      this.pathname.replace(/^\//,'') && 
      location.hostname === this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top-topoffset+1
        }, 800);
        return false;
      } //target.length
    } //click function
  }); //smooth scrolling


    // $('a.page-scroll').bind('click', function(event) {
    //     console.log("HERE");
    //     var $anchor = $(this);
    //     $('html, body').stop().animate({
    //         scrollTop: $($anchor.attr('href')).offset().top
    //     }, 1500, 'easeInOutExpo');
    //     event.preventDefault();
    // });


});